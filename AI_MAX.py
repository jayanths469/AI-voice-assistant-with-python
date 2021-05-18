import speech_recognition as sr
import pyttsx3
import wikipedia
import datetime
import os
import webbrowser
import smtplib
import pyaudio
from time import sleep
import random
import pyautogui

import os


MASTER = "Master"
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)

##Speak function will speak the give input.
def speak(text):
    engine.say(text)
    engine.runAndWait()

def wishing():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour<= 12:
        speak("Good Moring...." + MASTER )
    elif hour >=12 and hour <=18:
        speak("Good afternnon..." + MASTER)
    else:
        speak("Good evening.." + MASTER)

def takemastercomand():
    r = sr.Recognizer()
    with sr.Microphone() as Source:
        print("Lisiting......!!")
        audio = r.listen(Source)

        try:
            print("Recognizing")
            query = r.recognize_google(audio)
            print(f"User said : {query}\n")

        except Exception as error:
            print("Please say that again")
            query = None
    return query

def sendemail(to,content):
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('your ID','password')
    server.sendmail("test@gmail.com",to,content)
    server.close()


def main():
    wishing()
    x= "i am your voice assistant MAX....."
    speak("Hello")
    val = 10
    while val <= 10:
        speak("how may help you")
        query = takemastercomand()

        if 'wikipedia' in query.lower():
            speak('Searching wikipedia')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak(results)
            sleep(1)
        elif 'play music' in query.lower():
            songs_dir = r"C:\Alexacodes_Audio"
            songs = os.listdir(songs_dir)
            print(songs)
            speak("Playing Music from your library")
            os.startfile(os.path.join(songs_dir, songs[1]))
            sleep(1)

        elif 'open youtube' in query.lower():
            webbrowser.open('youtube.com', new=2)
            speak("Browser launched with youtube")
            print("Brower launched with youtube")
            sleep(1)

        elif "the time" in query.lower():
            time = datetime.datetime.now().strftime("%H:%M")
            speak(f"{MASTER} the time is {time}")
            sleep(1)

        elif "send email" in query.lower():
            try:
                speak("what should i send")
                content = takemastercomand()
                print("Whom should i send")
                speak("whom should i send")
                sleep(2)
                to = "Jayanths69@gmail.com" #your mail id
                sendemail(to, content)
                speak("email sent" + to)
                print("email sent to : " + to)
                sleep(1)

            except Exception as error:
                print(str(error))

        elif "calendar" in query.lower():
            speak("What date")
            date = takemastercomand()
            speak("What time")
            time = takemastercomand()
            speak(f"Calendar set busy on {date} at {time}")
            print(f"Calendar set busy on {date} at {time}")

        elif "who are you" in query.lower():
            speak("I am your AI assistant MAX.... i can play  music set calendar and send main i can do many more....")

        elif "where do you live" in query.lower():
            speak("I live here but my mind is in cloud but i am always available for you to help")

        elif "who designed you" in query.lower():
            speak("I was Designed by Jayanth sunkari in Hyderabad")

        elif "who is your boss" in query.lower():
            speak("You : you are my Master")

        elif "hi" in query.lower():
            OP = ['Hello','HI','Hola','Namstay']
            speak(random.choice(OP))


        elif "kill" in query.lower():
            speak("Have a good day, Chow....")
            break
    val += 1



main()