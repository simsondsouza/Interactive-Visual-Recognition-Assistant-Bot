import requests
import json
import pyttsx3   #Text to Speech
import time
def speak(audio): #Text to Speech
    tts = pyttsx3.init()  #Intialize the TTS Engine
    voices = tts.getProperty('voices')
    #[0]-> Male Voice, [1]->Female Voice in Set Property
    tts.setProperty('voice', voices[1].id)
    print("Speaking...")
    tts.say(audio) #Method for the assistant to speak
    tts.runAndWait() #Blocks while processing all the currently queued commands

def top_headlines():
    url = ('https://newsapi.org/v2/top-headlines?country=in&sortBy=popularity&apiKey=7a2f8ff672384a1fac893968cd0a018f')
    response = requests.get(url)
    result = response.json()
    extract(result)
    
def query(statement):
    url = ('https://newsapi.org/v2/everything?q={}&apiKey=7a2f8ff672384a1fac893968cd0a018f').format(statement)
    response = requests.get(url)
    result = response.json()
    extract(result)
    
def extract(result):
    i = 0
    while i < 5:
        description  = result['articles'][i]['description']
        i+=1
        speak(description)
        time.sleep(2)


