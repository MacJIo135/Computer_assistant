import ctypes
import os
import glob
import pywhatkit
from pygame import mixer

from Main import *


def open_program(command):
    program_name = command.split("відкрий")[1].strip()

    folder_path = f"C:\\Users\\golme\\OneDrive\\Рабочий стол"

    files = glob.glob(os.path.join(folder_path, f"{program_name}.*"))

    if files:
        program_path = files[0]
        try:
            os.startfile(program_path)
            speak(f"Окей, відкриваю {program_name}")
        except Exception as e:
            speak(f"Не вдалося відкрити: {e}")
    else:
        speak(f"{program_name} не вдалося знайти")


def write_to_file(command):
    text_to_write = command.split("пиши")[1].strip()
    try:
        with open("output.txt", "a") as file:
            file.write(text_to_write + "\n")
        speak("Text written to file.")
    except Exception as e:
        speak(f"Error writing to file: {e}")


def playing_music(command):
    song = command.split("включи")[1].strip()
    speak("Грає" + song)
    pywhatkit.playonyt(song)


def change_volume(volume):
    volume = max(0, min(volume, 100))
    ctypes.windll.user32.SendMessageW(0xFFFF, 0x319, volume, 0x20000)
    speak(f"Встановлено гучність на {volume}")


def hi(command):
    speak("Привіт, як ти?")


def thank_you(command):
    speak("Завжди до ваших послуг сер!")


def how_are_you(command):
    speak("Краще не буває, сподіваюсь у вас все добре")
