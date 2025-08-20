# 5.2.3. Проект Напоминание
# 5.2.4. Функция set
# 5.2.5. Функция check
# 5.2.6. Функция отключения музыки
# 5.2.7. Отображение времени напоминания
# 5.2.8. Отображение текста напоминания
# 5.2.9. Преобразуем проект в исполняемый файл
# 5.2.10. Совет по запуску исполняемого файла
# 5.2.11. Второй совет по расположению mp3

# Напоминание
# устанавливаем pygame C:\Python\Scripts\pip install pygame

from tkinter import *
from tkinter import simpledialog as sd
from tkinter import messagebox as mb
import datetime
import time
import pygame

t = None

def set():
    global t
    rem = sd.askstring("Время напоминания", "Введите время в формате ЧЧ:ММ (24-часовой формат)")
    if rem:
        try:
            hour = int(rem.split(":")[0])
            minute = int(rem.split(":")[1])
            now = datetime.datetime.now()
            print(now)
            dt = now.replace(hour=hour, minute=minute)
            print(dt)
            t = dt.timestamp()
            print(t)
            label.config(text=f"Напоминание установлено на: {hour:02}:{minute:02}")
        except ValueError:
            mb.showerror("Ошибка", "Неверный формат времени")

def check():
    global t
    if t:
        now = time.time()
        if now >= t:
            play_snd()
            t = None
    window.after(10000, check)

def play_snd():
    pygame.mixer.init()
    pygame.mixer.music.load("reminder.mp3")
    pygame.mixer.music.play()

window = Tk()
window.title("Напоминание")

label = Label(text="Установите напоминание", font=("Arial", 14))
label.pack(pady=10)

set_button = Button(text="Установить напоминание", command=set)
set_button.pack(pady=10)

check()

window.mainloop()