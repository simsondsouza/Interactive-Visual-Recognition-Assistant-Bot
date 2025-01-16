from datetime import datetime
import datefinder as df
import sys
import speech_recognition as sr  #Speech To text
import pyttsx3   #Text to Speech
import time

def audio_input(): #Speech to Text
    r = sr.Recognizer() #Initialize Speech Recognition Engine
    with sr.Microphone() as source: #Intialize Microphone
        print('Listening...')
        r.adjust_for_ambient_noise(source, duration=0.5)
        audio = r.listen(source, phrase_time_limit=5) #Capture Audio
        try: 
            statement = r.recognize_google(audio, language='en-in')
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

def remind(statement,msg):
    dateandtime = df.find_dates(statement)
    for i in dateandtime:
        time1 = i.strftime("%H:%M")

    while True:
        current_time = datetime.now().strftime("%H:%M")
        if current_time == time1:
            speak("Reminder" + msg)
            time.sleep(5)
            speak("Reminder" + msg)
            break
        elif current_time > time1:
            break
            
sentence = " ".join(sys.argv[1:])
msg = sentence.partition("m.")[2]   #Output: ('remind me at 11:48 a.', 'm.', ' turn on the light') without Indexing
remind(sentence,msg)