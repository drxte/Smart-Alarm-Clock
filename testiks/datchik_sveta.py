import machine
import time
import apds9960  # Импортируем наш простой файл
import ssd1306  # Импортируем библиотеку для работы с OLED-дисплеем

# 1. Запускаем I2C на твоих пинах (scl=7, sda=6)
i2c = machine.I2C(0, scl=machine.Pin(7), sda=machine.Pin(6))

# 2. Подключаем датчик света
sensor = apds9960.APDS9960(i2c)
oled = ssd1306.SSD1306_I2C(128, 32, i2c)  # Настраиваем OLED-дисплей
ledRed = machine.Pin(10, machine.Pin.OUT)
ledGreen = machine.Pin(11, machine.Pin.OUT)
ledBlue = machine.Pin(21, machine.Pin.OUT)  # Настраиваем встроенный светодиод

while True:
    oled.fill(0)  # Очищаем экран
    # 3. Считываем уровень освещенности (одной простой командой!)
    light_level = sensor.read_light()
    
    oled.text("Light: {}".format(light_level), 0, 0)  # Выводим уровень освещенности на экран
    oled.show()  # Обновляем экран

    if (light_level == 0):
        ledBlue.value(1)
        ledRed.value(1)
        ledGreen.value(0)
    else:
        ledBlue.value(0)
        ledRed.value(0)
        ledGreen.value(0)
    
    # Ждем полсекунды перед следующим замером
    time.sleep(0.5)
