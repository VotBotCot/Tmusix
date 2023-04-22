import pygame
import os
from mutagen.mp3 import MP3
from time import sleep as sl
import sys

music = ''
if len(sys.argv) > 1:
    music = sys.argv[1]
else:
    os.system("clear")
    music = input("Music: ")
    while music == "":
        os.system("clear")
        music = input("Music: ")
m = MP3(music)
pygame.init()
pygame.mixer.init()

# вывод частей трека,○-
progress_y = "○"
progress_n = "-"

# загрузим музыку
pygame.mixer.music.load(music)

# начнем проигрывание музыки и сделаем ее зацикленной
elapsed_seconds = 0
pygame.mixer.music.play()

length = round(m.info.length)

# основной цикл программы
while True:
    os.system("clear")
   # выводим информацию о времени и прогрессе
    elapsed_seconds = elapsed_seconds + 1
    total_seconds = length = round(m.info.length)
    remaining_seconds = total_seconds - elapsed_seconds
    if float(f"{elapsed_seconds/total_seconds:.2f}") == 1.0:
        break
    # рисуем прогресс-бар
    progress = float(f"{elapsed_seconds/total_seconds:.2f}")
    progress_bar = ""
    for i in range(10):
        if i*10  == round(progress*10)*10:
            progress_bar += progress_y
        else:
            progress_bar += progress_n
    print(music)
    print("{} | {:02d}:{:02d}/{:02d}:{:02d}".format(progress_bar, elapsed_seconds // 60, elapsed_seconds % 60, total_seconds // 60, total_seconds % 60))
    sl(1)
