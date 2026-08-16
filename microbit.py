import serial
import pyautogui
import speech_recognition as sr

# Adjust COM port for your micro:bit
ser = serial.Serial('COM3', 115200)
recognizer = sr.Recognizer()
mic = sr.Microphone()

while True:
    line = ser.readline().decode().strip()
    if line == "DICTATE":
        with mic as source:
            print("Listening...")
            audio = recognizer.listen(source)
        try:
            text = recognizer.recognize_google(audio)
            pyautogui.typewrite(text)
        except sr.UnknownValueError:
            pyautogui.typewrite("[Unrecognized speech]")
    elif line == "STOP":
        pyautogui.typewrite("\n[Dictation stopped]\n")

