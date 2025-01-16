import subprocess #runs another script while also running the main program 
import os
from urllib import response
import pyttsx3   #Text to Speech
import speech_recognition as sr  #Speech To text
import weathercom  
import webbrowser #extracts data from web
from time import sleep  #To add delay
from Features.date_time import day, time, date
from Features.weather_forecast import weatherReport
from Features.wikipedia_search import search
from Features.news import top_headlines, query

def audio_input(): #Speech to Text
    r = sr.Recognizer() #Initialize Speech Recognition Engine
    with sr.Microphone() as source: #Intialize Microphone
        print('Listening...')
        r.adjust_for_ambient_noise(source, duration=0.5)
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

#------------------------------------------------------------------------------------------

if __name__=='__main__':
    speak("Hey, What can I do for you")
    while True:
        statement = audio_input().lower()
        if "time" in statement:
            speak(time())

        elif "date" in statement:
            speak("The date is" + date())


        elif "weather" in statement:
            speak("which city")
            city = audio_input()   #Calling Audio Input Function for City Name
            humidity, temp, phrase = weatherReport(city) #Calling WeatherReport Function
            speak("currently in " + city + "  temperature is " + str(temp)
            + " degree celsius, " + "humidity is " + str(humidity) + " percent and sky is " + phrase)

        elif 'open youtube' in statement:
            webbrowser.open_new_tab("https://www.youtube.com") #open_new_tab function accepts URL as a parameter that needs to be accessed
            speak("youtube is open now")
            sleep(5)  #halt the execution of the program for given time in seconds

        elif 'open google' in statement:
            webbrowser.open_new_tab("https://www.google.com") #open_new_tab function accepts URL as a parameter that needs to be accessed
            speak("Google chrome is open now")
            sleep(5) #halt the execution of the program for given time in seconds

        elif 'open gmail' in statement:
            webbrowser.open_new_tab("gmail.com") #open_new_tab function accepts URL as a parameter that needs to be accessed
            speak("Google Mail open now")
            sleep(5) #halt the execution of the program for given time in seconds

        elif "goodbye" in statement or  "ok bye" in statement or "stop" in statement or "bye" in statement:
            speak("your personal assistant Robot is shutting down,Good bye")
            subprocess.Popen("python wake_up.py",shell=True)
            break       

        # elif "find" or "what is" or "search" or "google search" in statement:
        #     speak("This is what I found for you")
        #     speak(search(statement))

        elif "none" in statement:
            continue

        elif "alarm" in statement:
            speak("Alarm has been set")
            subprocess.Popen("python Features\Reminder\Alarm.py " + statement,shell=True)

        elif "news" in statement:
            if "search" in statement:
                query(statement) 
            elif "top headlines" or "news" in statement:
                top_headlines()            

        elif "reminder" in statement or "remind" in statement:
            speak("What should I remind you?")
            msg = audio_input()
            subprocess.Popen("python Features\Reminder\Remind.py " + statement + msg,shell=True)   

        elif "day" in statement:                
            speak("The day is" + day())  
            
        else:
            speak("Pardon me, please say that again")
            continue