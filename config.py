import buzzer
import display

buz = buzzer.Buzzer()
disp = display.Display()

def get_buzzer():
    return buz

def get_display():
    return disp

def get_oled():
    return disp.get_oled()
