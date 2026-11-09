import machine
import time
import drivers.apds9960 as apds9960

def nightlight():
    i2c = machine.I2C(0, scl=machine.Pin(7), sda=machine.Pin(6))
    
    sensor = apds9960.APDS9960(i2c)
    ledRed = machine.Pin(10, machine.Pin.OUT)
    ledGreen = machine.Pin(11, machine.Pin.OUT)
    ledBlue = machine.Pin(21, machine.Pin.OUT)
    
    while True:
        light_level = sensor.read_light()

        if (light_level == 0):
            ledBlue.value(1)
            ledRed.value(1)
            ledGreen.value(0)
        else:
            ledBlue.value(0)
            ledRed.value(0)
            ledGreen.value(0)
    
        time.sleep(0.5)