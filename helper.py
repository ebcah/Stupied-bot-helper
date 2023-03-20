from vosk import Model, KaldiRecognizer  
import speech_recognition  
import wave  
import json  
import os  
import webbrowser
import subprocess
import pyautogui
import keyboard
import time
import pyttsx3
engine = pyttsx3.init()
notasd=0

engine.say('добрый день')
engine.runAndWait()
def record_and_recognize_audio(*args: tuple):
    """
    Запись и распознавание аудио
    """
    with microphone:
        recognized_data = ""

        # регулирование уровня окружающего шума
        recognizer.adjust_for_ambient_noise(microphone, duration=3)

        try:
            print("Listening...")
            
            engine.runAndWait()
            audio = recognizer.listen(microphone, 5, 5)

            with open("microphone-results.wav", "wb") as file:
                file.write(audio.get_wav_data())

        except speech_recognition.WaitTimeoutError:
            print("Can you check if your microphone is on, please?")
            
            engine.runAndWait()
            return

        # использование online-распознавания через Google 
        try:
            print("Started recognition...")
            recognized_data = recognizer.recognize_google(audio, language="ru").lower()

        except speech_recognition.UnknownValueError:
            pass

        # в случае проблем с доступом в Интернет происходит попытка 
        # использовать offline-распознавание через Vosk
       

        return recognized_data







add=0



def functions(voice):
    global notasd
    if notasd==1:
        voice1=voice.lower()
        voice1=voice1.split(" ")
        print(voice1)
        for i in voice1:
            print("rabotaet")
            if i=="открой" or i=="відкрий" or i=="зайди" or i=="найди":
                for i in voice1:
                    if i=="браузер" or i=="google" or i == "опера" or i=="оперу" or i=="сайт" or i=="вкладку" or i=="youtube" or i=="ии":
                        if i=="браузер" or i=="google" or i == "опера" or i=="оперу":
                            webbrowser.open("https://www.google.com/", new=1, autoraise=True)
                            engine.say('открываю')
                            engine.runAndWait()
                            print("asd")
                        elif i=="youtube":
                            engine.say('открываю ютуб')
                            engine.runAndWait()
                            webbrowser.open("https://www.youtube.com/", new=0, autoraise=True)
                        elif i=="ии":
                            engine.say('Открываю чат гбт')
                            engine.runAndWait()
                            webbrowser.open("https://chat.openai.com/", new=0, autoraise=True)
                    
                    elif i!="открой" or i!="відкрий" or i!="зайди" or i!="найди" and i!="браузер" or i!="google" or i != "опера" or i!="оперу" or i!="сайт" or i!="вкладку" or i!="youtube" or i!="ии":
                        
                        engine.runAndWait()
                        global add
                        if add==0:
                            engine.say('Пытаюсь найти')
                            voice2=voice.split(i)
                            print(voice2[1])
                        
                            pyautogui.hotkey('win')   
                    
                            keyboard.write(voice2[1])
                    
                            
                            keyboard.press("enter")
                            time.sleep(0.1)
                            keyboard.release("enter")  
                            add+=1
                        else:
                            add-=1
                        time.sleep(2)
            elif i=="хватит":
                notasd-=1




    else:
        voice1=voice.lower()
        voice1=voice1.split(" ")
        for i in voice1:
            if i=="привет":
                print("asd")
                notasd-=notasd
                notasd+=1
                engine.say('я вас слушаю если хотите окончить, скажите хватит')
        
            
            

    









if __name__ == "__main__":
    engine.say('Скажи приевт если я тебе понадоблюсь и хватит если хочешь временно остановить')
    
    # инициализация инструментов распознавания и ввода речи
    recognizer = speech_recognition.Recognizer()
    microphone = speech_recognition.Microphone()

    while True:
        # старт записи речи с последующим выводом распознанной речи
        # и удалением записанного в микрофон аудио
        voice_input = record_and_recognize_audio()
        
        print(voice_input)
        try:
            functions(voice_input)
        except:
            ...
        
    