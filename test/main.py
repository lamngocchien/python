import pyttsx3
import speech_recognition as sr

def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Robot: I'm listening...")
        r.adjust_for_ambient_noise(source)
        # audio = r.record(source, duration=3)
        audio = r.listen(source)
        try:
            text = r.recognize_google(audio)
            # text = r.recognize_google(audio, language='vi-VN')
        except:
            text = ""
    print('Text:', text)
    return text

def main():
    while True:
        text = listen()
        speak(text)
        if text == 'goodbye':
            break

main()