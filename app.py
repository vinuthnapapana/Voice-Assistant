import datetime
import random
import re
import smtplib
import subprocess
import sys
import time
import webbrowser
import json

import pyautogui
import pyjokes
import pyttsx3
import pywhatkit
import requests
import speech_recognition as sr
import ti as ti
import wikipedia

import winshell
import wolframalpha
#from secrets import senderemail, password
engine = pyttsx3.init('sapi5')

client = wolframalpha.Client('Your_App_ID')

voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
def speak(audio):
    print('Benn: ' + audio)
    engine.say(audio)
    engine.runAndWait()
def wishMe():
    hour=datetime.datetime.now().hour
    if hour>=0 and hour<12:
        speak("Hello,Good Morning")
        print("Hello,Good Morning")
    elif hour>=12 and hour<16:
        speak("Hello,Good Afternoon")
        print("Hello,Good Afternoon")
    else:
        speak("Hello,Good Evening")
        print("Hello,Good Evening")
wishMe()
speak("I am your Assistant Benn")
speak("How may I help you")
def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('chilukuri.praneethareddy@gmail.com', '9000039008')
    server.sendmail('chilukuri.praneethareddy@gmail.com', to, content)
    server.close()
def myCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Initialising...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        query = r.recognize_google(audio, language='en-in')
        print('User: ' + query + '\n')

    except sr.UnknownValueError:
        speak('Sorry Mam! I did not get that! Try typing the command!  I will check it out')
        query = str(input('Command: '))
    return query
if __name__ == '__main__':
   while True:

        query = myCommand()
        query = query.lower()


        if'open'and'youtube' in query:
            speak('okay mam')
            webbrowser.open('www.youtube.com')
            time.sleep(5)
        elif 'play the song' in query:
            song = query.replace('play', '')
            speak('playing ' + song)
            pywhatkit.playonyt(song)
            time.sleep(5)
        elif 'open'and'google'in query:
            speak('okay mam')
            webbrowser.open('www.google.co.in')
            time.sleep(5)
        elif 'open'and'whatsapp' in query:
            speak('okay mam')
            webbrowser.open('web.whatsapp.com')
            time.sleep(5)

        elif "show note" in query:
            speak("Showing Notes")
            file = open("hello", "r")
            print(file.read())
            speak(file.read(6))
            time.sleep(5)
        elif "take a screenshot" in query:
            pyautogui.screenshot("{0}.png".format(str(time.time()))).show()
            time.sleep(5)
        elif 'send an email' in query:
            try:
                speak("What should I say?")
                content = myCommand()
                to = "vinuthna.papana8@gmail.com"
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry mam. I am not able to send this email")
        elif 'compute' in query:
            speak('I can answer to computational and geographical questions  and what question do you want to ask now')
            question = myCommand()
            app_id = "2JE2AT-99X3L9V892"
            client = wolframalpha.Client('R2K75H-7ELALHR35X')
            res = client.query(question)
            answer = next(res.results).text
            speak(answer)
            print(answer)
        elif "weather forecast" in query:
            api_key = "9323307c0b343645282266f8861b9c5d"
            base_url = "https://home.openweathermap.org/home?"
            speak("what is the city name")
            city_name = myCommand()
            complete_url = base_url + "appid=" + api_key + "&q=" + city_name
            response = requests.get(complete_url)
            x = response.json()
            if x["cod"] != "404":
                y = x["main"]
                current_temperature = y["temp"]
                current_humidity = y["humidity"]
                z = x["weather"]
                weather_description = z[0]["description"]
                speak(" Temperature in kelvin unit is " +
                      str(current_temperature) +
                      "\n humidity in percentage is " +
                      str(current_humidity) +
                      "\n description  " +
                      str(weather_description))
                print(" Temperature in kelvin unit = " +
                      str(current_temperature) +
                      "\n humidity (in percentage) = " +
                      str(current_humidity) +
                      "\n description = " +
                      str(weather_description))
        elif 'open'and'gmail' in query:
            speak('okay mam')
            webbrowser.open('www.gmail.com')
            time.sleep(5)
        elif 'open java t point' in query:
            webbrowser.open("www.javatpoint.com")
            time.sleep(5)
        elif 'send whatsapp message' in query:
            pywhatkit.sendwhatmsg_instantly('+91 9640756791', 'hello', 10, None, False)
            time.sleep(5)
        elif 'what is the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Mam the time is {strTime}")
            time.sleep(5)
        elif 'when were you born' in query:
            speak("I was created on 10th July 2021 by Vinuthna ")
            time.sleep(5)
        elif 'why were you created' in query:
            speak("I was created for making her work simpler")
            time.sleep(5)
        elif 'wait'and'for'and 'a'and 'minute' in query:
            speak('okay mam')
            time.sleep(60)
        elif "what\'s up" in query or 'how are you' in query:
            stMsgs = ['Just doing my thing!', 'I am fine!', 'Nice!', 'I am nice and full of energy']
            speak(random.choice(stMsgs))
            time.sleep(5)
        elif 'tell me a joke' in query:
            speak(pyjokes.get_joke())
            time.sleep(5)
        elif 'its a bad joke' in query:
            speak("Sorry mam, thats what i have....")
            time.sleep(5)
        elif "log off" in query or "shut down" in query:
            speak("Ok , your pc will log off in 10 sec make sure you exit from all applications")
            subprocess.call(["shutdown", "/l"])
        elif 'empty recycle bin' in query:
            winshell.recycle_bin().empty(confirm=False, show_progress=False, sound=True)
            speak("Recycle Bin is Recycled mam")
            time.sleep(5)
        elif "don't listen to me for sometime" in query or "stop listening to me for some time " in query:
            speak("for how much time you want to stop benn from listening commands")
            a = int(myCommand())
            time.sleep(a)
            print(a)
        elif "restart the system " in query:
            speak('yes mam the system is getting restarted hold on for a second ')
            subprocess.call(["shutdown", "/r"])
        elif "log off the system benn" in query or "sign out" in query:
            speak("Make sure all the application are closed before sign-out mam")
            time.sleep(5)
            subprocess.call(["shutdown", "/l"])
        elif 'okay'and'benn'and'bye' in query or 'abort' in query or 'stop' in query:
            speak('okay mam')
            speak('Bye mam, have a good day.')

            sys.exit()
        elif 'what is your name' in query:
            speak("My name is benn, I am your personal assistant")
        elif 'open' in query:
            reg_ex = re.search('open (.+)', query)
            if reg_ex:
                domain = reg_ex.group(1)
                print(domain)
                url = 'https://www.' + domain
                webbrowser.open(url)
                speak('The website you have requested has been opened for you mam.')
                time.sleep(5)
            else:
                pass
        elif 'fetch todays news' in query:
            news = webbrowser.open_new_tab('https://timesofindia.indiatimes.com/defaultinterstitial.cms')
            speak('Here are some headlines from the Times of India,Happy reading')
            time.sleep(6)
        elif 'search' in query:
            query = query.replace("search", "")
            webbrowser.open_new_tab(query)
            time.sleep(5)
        else:
            query = query
            speak('Searching...')
            try:
                try:
                    res = client.query(query)
                    results = next(res.results).text
                    speak('WOLFRAM-ALPHA says - ')
                    speak('Got it.')
                    speak(results)

                except:
                    results = wikipedia.summary(query, sentences=2)
                    speak('Got it.')
                    speak('WIKIPEDIA says - ')
                    speak(results)

            except:
                webbrowser.open('www.google.com')


        speak('Next Command!')