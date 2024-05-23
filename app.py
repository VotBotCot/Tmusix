import os
from mutagen.mp3 import MP3
from time import sleep as sl
import sys    
import random
from playsound import playsound
import threading

key_3 = ""

music = ''
if "-h" in sys.argv:
    print("Usage:")
    print("python tmusix.py <music_path> [options]")
    print("Options:")
    print("-e: Exit after finishing the current song.")
    print("-l: Restart the current song.")
    sys.exit()
if len(sys.argv) > 1:
    music = sys.argv[1]
else:
    os.system("clear")
    music = input("Music: ")
    while music == "":
        os.system("clear")
        music = input("Music: ")
        
if len(sys.argv) > 2:
    key_3 = sys.argv[2]

if os.path.isdir(music):
    # находим все файлы в папке, имеющие расширение .mp3
    music_files = [os.path.join(music, f) for f in os.listdir(music) if os.path.isfile(os.path.join(music, f)) and f.lower().endswith(".mp3")]
    if music_files:
        # выбираем случайный файл
        music = random.choice(music_files)
    else:
        # если в папке нет mp3-файлов, выводим сообщение об ошибке
        print("Error: no music files found in the specified directory.")
        sys.exit()

m = MP3(music)

# вывод частей трека
progress_y = "○"
progress_h = "—"
progress_n = "-"

elapsed_seconds = 0
length = round(m.info.length)

# Функция для воспроизведения музыки в отдельном потоке
def play_music():
    while True:
        playsound(music)

# Запускаем поток для воспроизведения музыки
music_thread = threading.Thread(target=play_music, daemon=True)
music_thread.start()

try:
    while True:
        os.system("clear")
        total_seconds = round(m.info.length)
        remaining_seconds = total_seconds - elapsed_seconds
        if float(f"{elapsed_seconds/total_seconds:.2f}") >= 1.0:
            if key_3 == "-e":
                break
            elif key_3 == "-l":
                elapsed_seconds = 0
            else:
                music = os.path.dirname(music)
                if os.path.isdir(music):
                    # находим все файлы в папке, имеющие расширение .mp3
                    music_files = [os.path.join(music, f) for f in os.listdir(music) if os.path.isfile(os.path.join(music, f)) and f.lower().endswith(".mp3")]
                    if music_files:
                        # выбираем случайный файл
                        music = random.choice(music_files)
                        elapsed_seconds = 0
                    else:
                        # если в папке нет mp3-файлов, выводим сообщение об ошибке
                        print("Error: no music files found in the specified directory.")
                        sys.exit()

        # рисуем прогресс-бар
        progress = float(f"{elapsed_seconds/total_seconds:.2f}")
        progress_bar = ""
        for i in range(10):
            if i*10 == round(progress*10)*10:
                progress_bar += progress_y
            elif i*10 < round(progress*10)*10:
                progress_bar += progress_h
            else:
                progress_bar += progress_n
        print(music)
        print("{} | {:02d}:{:02d}/{:02d}:{:02d}".format(progress_bar, elapsed_seconds // 60, elapsed_seconds % 60, total_seconds // 60, total_seconds % 60))
        sl(1)
        # выводим информацию о времени и прогрессе
        elapsed_seconds += 1
except KeyboardInterrupt:
    print('Bye bye...')
    os._exit(0)
