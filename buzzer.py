
import machine

class Buzzer:
    def __init__(self, pin=5):
        self.pin = machine.Pin(pin, machine.Pin.OUT)

        # Создаем PWM
        self.buz = machine.PWM(self.pin, freq=2000)

        self.MIN_LEVEL = 0
        self.MAX_LEVEL = 100

        # Начальная громкость
        self.volume = 40

        self.isOn = False

        # ВАЖНО: сразу выключаем звук
        self.buz.duty_u16(0)

    def on(self):
        if self.volume > 0:
            self.buz.duty_u16(
                int(self.volume * 65535 / 100)
            )
            self.isOn = True

    def off(self):
        self.buz.duty_u16(0)
        self.isOn = False

    def add_volume(self):
        self.volume += 20

        if self.volume > self.MAX_LEVEL:
            self.volume = self.MAX_LEVEL

        if self.isOn:
            self.on()

    def reduce_volume(self):
        self.volume -= 20

        if self.volume < self.MIN_LEVEL:
            self.volume = self.MIN_LEVEL

        if self.isOn:
            self.on()

    def get_volume(self):
        return self.volume

    def get_buzzer(self):
        return self.buz