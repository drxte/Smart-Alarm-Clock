import machine
import ssd1306
import time

# Настраиваем пин зуммера (поставь пин, который у тебя подписан, например 20)
buzzer = machine.PWM(machine.Pin(5))  # Замените 20 на номер пина, к которому подключен зуммер

# Частоты нот (в Герцах), которые нужны для кузнечика
A5 = 880   # Ля
E5 = 659   # Ми
C6 = 1047  # До шестой октавы
B5 = 988   # Си

# Длительности звуков (в секундах)
quarter = 0.4  # Четвертная нота (длинная)
eighth = 0.2   # Восьмая нота (короткая)

# Функция для проигрывания одной ноты
def play_note(freq, duration):
    buzzer.freq(freq)
    buzzer.duty(512)            # Включаем звук (50% громкости)
    time.sleep(duration)        # Ждем, пока нота звучит
    buzzer.duty(0)              # Выключаем звук
    time.sleep(0.03)            # Маленькая пауза между нотами, чтобы они не сливались

# Массив нот и их длительностей (Куплет)
melody = [
    (A5, eighth), (E5, eighth), (A5, eighth), (E5, eighth), (A5, eighth), (B5, quarter), (B5, quarter),
    (B5, eighth), (E5, eighth), (B5, eighth), (E5, eighth), (B5, eighth), (A5, quarter), (A5, quarter),
    (A5, eighth), (E5, eighth), (A5, eighth), (E5, eighth), (A5, eighth), (B5, quarter), (B5, quarter),
    (B5, eighth), (E5, eighth), (B5, eighth), (E5, eighth), (B5, eighth), (A5, quarter), (A5, quarter),
    
    # Припев ("Представьте себе...")
    (A5, eighth), (C6, quarter), (C6, quarter), (C6, eighth), (C6, eighth), (C6, eighth), (B5, eighth), (A5, eighth), (G5 if 'G5' in locals() else 784, quarter), (G5 if 'G5' in locals() else 784, quarter),
    (G5 if 'G5' in locals() else 784, eighth), (B5, quarter), (B5, quarter), (B5, eighth), (B5, eighth), (B5, eighth), (A5, eighth), (G5 if 'G5' in locals() else 784, eighth), (A5, quarter), (A5, quarter)
]

print("Играю: В траве сидел кузнечик...")

# Проигрываем всю мелодию по очереди
for note, duration in melody:
    play_note(note, duration)

print("Мелодия завершена!")