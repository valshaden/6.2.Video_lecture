# 5.2.3. Проект Напоминание

# Напоминание
# устанавливаем pygame C:\Python\Scripts\pip install pygame

from tkinter import *
from tkinter import simpledialog as sd
from tkinter import messagebox as mb
import datetime
import time
import pygame

window = Tk()
window.title("Напоминание")

label = Label(text="Установите напоминание", font=("Arial", 14))
label.pack(pady=10)

set_button = Button(text="Установить напоминание", command=set)
set_button.pack(pady=10)

window.mainloop()