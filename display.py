import ssd1306
import machine
import config

class Display:
    def __init__(self):
        i2c = machine.I2C(scl=machine.Pin(7), sda=machine.Pin(6))
        self.oled = ssd1306.SSD1306_I2C(128, 32, i2c)
        self.oled.fill(0)
        self.oled.show()

    def get_oled(self):
        return self.oled

    def show_time(self):
        rtc = machine.RTC()
        current_time = rtc.datetime()
        time_str = "{:02d}:{:02d}:{:02d}".format(current_time[4], current_time[5], current_time[6])
        self.oled.fill(0)
        self.oled.text(time_str, 35, 10)
        self.oled.show()

    def alarm_clock_screen(self):
        self.oled.fill(0)
        self.oled.text("Alarm Clock", 15, 10)
        self.oled.show()

    def volume_screen(self):
        self.oled.fill(0)
        self.oled.text("Volume", 40, 10)
        self.oled.show()

    def volume_level_screen(self):
        self.oled.fill(0)

        self.oled.text("Volume " + str(config.get_buzzer().get_volume()), 4, 10)
        #Внешний прямоугольник
        self.oled.line(5, 17, 123, 17, 1) 
        self.oled.line(5, 27, 123, 27, 1)
        self.oled.line(5, 17, 5, 27, 1)
        self.oled.line(123, 17, 123, 27, 1)

        #Уровень громкости

        #квадрат уже готов, но нужно нарисовать заполнение в зависимости от уровня громкости.
        volume_level = (500 - config.get_buzzer().get_volume()) / 100

        line = 11
        for i in range(21):
            self.oled.line(6, line, 20 * volume_level, line, 1)
            line += 1

        self.oled.show()

    def music_screen(self):
        self.oled.fill(0)
        self.oled.text("Music", 45, 10)
        self.oled.show()