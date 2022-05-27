import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib

a="ravikant"
engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)
def speak(text):
    engine.say(text)
    engine.runAndWait()

def wish():
    h=int(datetime.datetime.now().hour)

    if h>0 and h<12:
        speak("Good Morning" + a)
    elif h>=12 and h<16:
        speak("Good Afternoon" + a)
    else:
        speak("Good Evening" + a)

    speak("I am Rahul, How may I help you")
    
def inputcomand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening.....")
        audio=r.listen(source)
    
    try:
        print("Recognizing...")
        qu=r.recognize_google(audio,language='en-in')
        print(f"user said: {qu}\n")
    except Exception as e:
        print("Error in listening your voice")
        qu=None
    return qu

def sendmail(to,body):
    server=smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('yourail@gmail.com', 'akant as a password')
    server.sendail("rbkantshara@gmail.com",to,body)
    server.close()

def main():
    speak("Initialization...................")
    wish()
    s=inputcomand()
    if 'wikipedia' in s.lower():
        speak("Searching Wikipedia....")
        s=s.replace("wikipedia","")
        t=wikipedia.sumary(s,sentences=2)
        speak(t)

    elif 'open youtube' in s.lower():
        url='youtube.com'
        cp="C:\Program Files (x86)\Google\Chrome\Application\chrome.exe %s"
        webbrowser.get(cp).open(url)

    elif 'open google' in s.lower():
        url='google.com'
        cp="C:\Program Files (x86)\Google\Chrome\Application\chrome.exe %s"
        webbrowser.get(cp).open(url)

    elif 'open facebook' in s.lower():
        url='facebook.com'
        cp="C:\Program Files (x86)\Google\Chrome\Application\chrome.exe %s"
        webbrowser.get(cp).open(url)

    elif 'open instagram' in s.lower():
        url='instagram.com'
        cp="C:\Program Files (x86)\Google\Chrome\Application\chrome.exe %s"
        webbrowser.get(cp).open(url)

    elif 'the time' in s.lower():
        time=datetime.datetime.now().strftime("%H:%M:%S")
        speak(f"{a} the time is {time}")

    # elif 'play music' in s.lower():
    #     songs= path of the songs in your computer
    #     song=os.listdir(songs)
    #     os.startfile(os.path.join(songs,song[0]))

    elif 'open vscode' in s.lower():
        path="C:\\Users\\akant\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Visual Studio Code\\code.exe"
        os.startfile(path)

    elif 'eail to a' in s.lower():
        try:
            speak("What is needed to be send Sir")
            body=inputcomand()
            to='rbkantsharma@gail.com'
            sendmail(to,body)
            speak("Your eail has been send sir")
        
        except Exception as e:
            print(e)

main()