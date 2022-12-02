from Body.Listen import Listen
from Body.Speak import Speak
from Brain.Brain import ReplyBrain
from Brain.QNA import Questionans

import pyttsx3
import speech_recognition as sr
 
def Listen():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source,0,8)
        try:
            print("recognizing...")
            data = recognizer.recognize_google(audio,language='en-in')
            print(f"You said : {data}")
   
        except:
            return ""
        data = str(data)
        return data.lower()
def Speak(x):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice',voices[1].id)
    rate = engine.getProperty("rate")
    engine.setProperty('rate',168)
    engine.say(x)
    engine.runAndWait()


def Main():
    while True:
        Data = Listen()
        Data = str(Data)
        if "what is" in Data or "Where is" in Data or "how many" in Data or "who is" in Data:
            Reply = Questionans(Reply)
        
        elif "my location" in Data:
            from Google_Map.Map import map
            map()
        elif "exit " in Data:
            Speak("ok Rehan , I am exit now.")   
        else:
            pass
        Reply = ReplyBrain(Data)
        print(Reply)
        Speak(Reply)
        break
Main()
