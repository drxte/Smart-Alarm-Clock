import machine
import time

class APDS9960:
    def __init__(self, i2c, address=0x39):
        self.i2c = i2c
        self.address = address
        # Будим датчик и включаем свет (ALS)
        self.i2c.writeto_mem(self.address, 0x80, b'\x03')
        # Задаем скорость замера
        self.i2c.writeto_mem(self.address, 0x81, b'\xFF')

    def read_light(self):
        # Читаем 2 байта данных света
        data = self.i2c.readfrom_mem(self.address, 0x94, 2)
        # Просто переводим байты в обычное число
        return data[0] + (data[1] * 256)
