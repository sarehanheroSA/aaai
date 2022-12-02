import requests
import pyttsx3

def Speak(x):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice',voices[1].id)
    rate = engine.getProperty("rate")
    engine.setProperty('rate',168)
    engine.say(x)
    engine.runAndWait()

def map():

    ip_add = requests.get('https://api.ipify.org/').text

    url = 'https://get.geojs.io/v1/ip/geo/' + ip_add + '.json'

    R = requests.get(url)
    R = R.json()

    state = R['city']

    country = R['country']
    print(state , country)
    Speak(f"sir , You Are Now In {state , country} .")
    






