import config
import time

class Alarm:
    def __init__(self):
        self.buzzer = config.get_buzzer()
        self.melody = 1

    def set_volume(self, volume):
        if self.buzzer.get_volume() == 500:
            return volume
        else:
            return volume * (self.buzzer.get_volume() / 500)

    def play_note(self, freq, duration):
        self.buzzer.freq(freq)
        self.buzzer.duty(512)
        time.sleep(duration)
        self.buzzer.duty(0)
        time.sleep(0.03)

    def melody_1(self):
        A5 = 880
        E5 = 659
        C6 = 1047
        B5 = 988
        G5 = 784

        quarter = 0.4
        eighth = 0.2

        melody = [
            (A5, eighth), (E5, eighth), (A5, eighth), (E5, eighth), (A5, eighth), (B5, quarter), (B5, quarter),
            (B5, eighth), (E5, eighth), (B5, eighth), (E5, eighth), (B5, eighth), (A5, quarter), (A5, quarter),
            (A5, eighth), (E5, eighth), (A5, eighth), (E5, eighth), (A5, eighth), (B5, quarter), (B5, quarter),
            (B5, eighth), (E5, eighth), (B5, eighth), (E5, eighth), (B5, eighth), (A5, quarter), (A5, quarter),

            (A5, eighth), (C6, quarter), (C6, quarter), (C6, eighth), (C6, eighth), (C6, eighth), (B5, eighth), (A5, eighth), (G5, quarter), (G5, quarter),
            (G5, eighth), (B5, quarter), (B5, quarter), (B5, eighth), (B5, eighth), (B5, eighth), (A5, eighth), (G5, eighth), (A5, quarter), (A5, quarter)
        ]

        print("Играю: В траве сидел кузнечик...")

        # Проигрываем всю мелодию по очереди
        for note, duration in melody:
            self.play_note(note, duration)

        print("Мелодия завершена!")

alarm = Alarm()
alarm.melody_1()