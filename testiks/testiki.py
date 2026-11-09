import machine
import drivers.ssd1306 as ssd1306
import network
import time
import socket
import struct

i2c = machine.I2C(0, scl=machine.Pin(7), sda=machine.Pin(6))
oled = ssd1306.SSD1306_I2C(128, 32, i2c)
buzzer = machine.PWM(machine.Pin(5)) 
buzzer.duty(0)
button = machine.Pin(2, machine.Pin.IN, machine.Pin.PULL_UP)  # Настраиваем кнопку с подтяжкой к питанию

ALARM_HOUR = 21
ALARM_MINUTE = 18

def connect_to_wifi():
    wlan = network.WLAN(network.STA_IF)
    wlan.active(False)
    wlan.active(True)
    wlan.connect("iPhone KY", "ovtu4144")

    a = "."
    while not wlan.isconnected():
        oled.fill(0)
        if a == "....":
            a = "."
        oled.text("Connecting" + a, 10, 5)
        oled.show()
        a += "."
        time.sleep(0.5)

    oled.fill(0)
    oled.text("Connected!", 10, 5)
    oled.show()
    time.sleep(1)

def get_time_from_ntp():
    addr = socket.getaddrinfo("pool.ntp.org", 123)[-1][-1]
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.settimeout(2)

    NTP_QUERY = b'\x1b' + b'\x00' * 47
    s.sendto(NTP_QUERY, addr)

    msg, r_addr = s.recvfrom(48)
    s.close()

    val = struct.unpack("!I", msg[40:44])[0]
    net_seconds = val - 3155673600

    TIMEZONE_OFFSET = 1 * 3600 
    final_seconds = net_seconds + TIMEZONE_OFFSET

    tm = time.localtime(final_seconds)
    machine.RTC().datetime((tm[0], tm[1], tm[2], tm[6] + 1, tm[3], tm[4], tm[5], 0))
    oled.fill(0)
    oled.text("Time updated!", 10, 5)
    oled.show()
    time.sleep(1)

    # Флаг, который показывает, активен ли сейчас будильник
    alarm_active = False

    while True:
        now = time.localtime()
        time_string = "{:02d}:{:02d}:{:02d}".format(now[3], now[4], now[5])

        oled.fill(0)
        oled.text(time_string, 10, 10)
        
        if alarm_active:
            oled.text("ALARM!!!", 80, 10)
        oled.show()

        # Триггер будильника (срабатывает в 00 секунд заданной минуты)
        if now[3] == ALARM_HOUR and now[4] == ALARM_MINUTE and now[5] == 0:
            alarm_active = True

        # ПРОВЕРКА НАЖАТИЯ КНОПКИ ДЛЯ ВЫКЛЮЧЕНИЯ
        # Если будильник активен И кнопка нажата (выдаёт 0)
        if alarm_active and button.value() == 0:
            alarm_active = False
            buzzer.duty(0) # На всякий случай глушим звук сразу
            oled.fill(0)
            oled.text("Alarm OFF!", 10, 10)
            oled.show()
            time.sleep(1.5) # Пауза, чтобы надпись успели прочитать

        # Логика пищания без зависания
        if alarm_active:
            buzzer.freq(880)
            buzzer.duty(512)  
            time.sleep(0.2)   
            buzzer.duty(0)    
            time.sleep(0.8)   
    else:
        # Если будильник не активен, просто спим 1 секунду до следующего обновления времени
        time.sleep(1)

# ---СТАРТ---
oled.fill(0)
oled.text("Hello!", 10, 5)
oled.show()
time.sleep(1)

connect_to_wifi()
get_time_from_ntp()
