import pygame
import speech_recognition as sr
from functions import *
from gtts import gTTS


ASSISTANT_NAME = "джарвіс"


def listen():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source, duration=1)
        audio = recognizer.listen(source)

    try:
        print("Recognizing...")
        command = recognizer.recognize_google(audio, language="uk-UA").lower()
        parts = command.split(ASSISTANT_NAME)
        if len(parts) > 1:
            command = parts[1].strip()
        print("You said: " + command)
        return command
    except sr.UnknownValueError:
        print("Sorry, could not understand your audio.")
        return None
    except sr.RequestError as e:
        print(f"Could not request results from Google Speech Recognition service; {e}")
        return None


def speak(text):
    tts = gTTS(text=text, lang='uk', slow=False)
    tts.save("output.mp3")
    pygame.init()
    pygame.display.set_mode((1, 1), pygame.NOFRAME)

    try:
        pygame.mixer.music.load("output.mp3")
        pygame.mixer.music.play()

        while pygame.mixer.music.get_busy():
            pygame.time.Clock().tick(10)

    finally:
        pygame.mixer.music.stop()
        pygame.quit()


def process_command(command):
    if command is not None:
        if "відкрий" in command:
            open_program(command)
        elif "запиши" in command:
            write_to_file(command)
        elif "включи" in command:
            playing_music(command)
        elif "привіт" in command:
            hi(command)
        elif "як ти" in command:
            how_are_you(command)
        elif "дякую" in command:
            thank_you(command)
        elif "гучність" in command:
            parts = command.split()
            if len(parts) > 1 and parts[1].isdigit():
                volume = int(parts[1])
                change_volume(volume)
            else:
                speak("Будь ласка, вкажіть після гучність бажаний рівень числом")
        else:
            print("Не знайома команда.")


if __name__ == "__main__":
    while True:
        user_command = listen()
        process_command(user_command)
