from pip import main
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
    #------------------------------------------------------------------
    #To find time from the spoken phrase
    dateandtime = df.find_dates(statement)
    for i in dateandtime:
        time = i.strftime("%H:%M")
    #-------------------------------------------------------------------

    #------------------------------------------------------------------
    #To append data to the text file
    file = open("C:\\Users\\Simson\\OneDrive\\Desktop\\Project\\Features\\Reminder\\data.txt", "a")
    #Opens a file for appending at the end of the file without truncating it. Creates a new file if it does not exist.
    file.write(time + "\n")
    file.close()
    #------------------------------------------------------------------

    #------------------------------------------------------------------
    #To read data from the file and play the sound
    file = open("C:\\Users\\Simson\\OneDrive\\Desktop\\Project\\Features\\Reminder\\data.txt", "r")
    line = file.read().split('\n')  #To get a list of elements
    file.close()
    print(line)
    while True:
        current_time = datetime.now().strftime("%H:%M")
        for i in line:
            if current_time == i:
                playsound("C:\\Users\\Simson\\OneDrive\\Desktop\\Project\\Features\\Reminder\\wakeup.mp3")
                a = audio_input().lower()
                if "none" in a:
                    continue
                elif "stop" or "turn off" in a:
                    speak("Turning Off the Alarm")
                    line.remove(i)
                    del_element(i)
                    break
            elif current_time > i:
                line.remove(i)
                del_element(i)
                break
    #------------------------------------------------------------------

def del_element(ele):
    file = open("C:\\Users\\Simson\\OneDrive\\Desktop\\Project\\Features\\Reminder\\data.txt", "w+")
    line = file.readlines()
    for i in line:
        if i.find(ele) == -1:   #Find returns -1 if match not found
            file.write(i)
    # line = line.remove(ele)
    # file.write(line)
    file.close()

sentence = " ".join(sys.argv[1:])

alarm("set alarm of 9:55 pm")