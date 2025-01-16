from playsound import playsound
from datetime import datetime
import datefinder as df
import sys
import speech_recognition as sr  #Speech To text
import pyttsx3   #Text to Speech

def audio_input(): #Speech to Text
    r = sr.Recognizer() #Initialize Speech Recognition Engine
    with sr.Microphone() as source: #Intialize Microphone
        print('Listening...')
        audio = r.listen(source, phrase_time_limit=5) #Capture Audio
        try: 
            statement = r.recognize_google(audio, language='en-in')
            print("user said:" + statement)
        except Exception as e:
            return "None"
        return statement


def speak(audio): #Text to Speech
    tts = pyttsx3.init()  #Intialize the TTS Engine
    voices = tts.getProperty('voices')
    #[0]-> Male Voice, [1]->Female Voice in Set Property
    tts.setProperty('voice', voices[1].id)
    print("Speaking...")
    tts.say(audio) #Method for the assistant to speak
    tts.runAndWait() #Blocks while processing all the currently queued commands

def alarm(statement):
    dateandtime = df.find_dates(statement)
    for i in dateandtime:
        time = i.strftime("%H:%M")

    while True:
        current_time = datetime.now().strftime("%H:%M")
        if current_time == time:
            playsound("C:\\Users\\Simson\\OneDrive\\Desktop\\Project\\Features\\Reminder\\wakeup.mp3")
            a = audio_input().lower()
            if "none" in a:
                continue
            elif "stop" or "turn off" in a:
                speak("Turning Off the Alarm")
                break
        elif current_time > time:
            break

sentence = " ".join(sys.argv[1:])
alarm(sentence)

