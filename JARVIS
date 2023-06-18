from win32com.client import Dispatch
import requests
import speech_recognition as sr
import webbrowser
import datetime
import pywhatkit
import pyttsx3
import smtplib, ssl

listener = sr.Recognizer()

def gettime():
    return datetime.datetime().now().hour()

engine = pyttsx3.init()
voices = engine.getProperty("voices")
engine. setProperty("rate", 150)
engine.setProperty("voice", voices[1].id)

def SpeakTest(command):
    engine.say(command)
    engine.runAndWait()
    

def takecommand(text):
    if "play" in text:
        song = text.replace("play","")
        print(text)
        SpeakTest("Playing")
        pywhatkit.playonyt(song)
    # elif "mail" in text:
    #     print(text)
    #     port = 465  # For SSL
    #     smtp_server = "smtp.gmail.com"
    #     sender_email = "decipher297@gmail.com"  # Enter your address
    #     receiver_email = "tanmoysaha2002@gmail.com"  # Enter receiver address
    #     password = "abcdd@2002."
    #     message = "Hey dude! It is an automated message."

    #     context = ssl.create_default_context()
    #     with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
    #         server.login(sender_email, password)
    #         server.sendmail(sender_email, receiver_email, message)
    

hour = int(datetime.datetime.now().hour)
if hour>0 and hour<=12:
    SpeakTest("GOOD MORNING")
elif hour>12 and hour<=18:
    SpeakTest("GOOD AFTERNOON")
elif hour>18 and hour<=24:
    SpeakTest("GOOD EVENING")

SpeakTest("HELLO! I'M JARVIS, YOUR PERSONAL ASSISTANT AT YOUR SERVICE")
print("CAN I KNOW YOUR NAME?")
SpeakTest("CAN I KNOW YOUR NAME?")
s = input()
SpeakTest(f"WELCOME {s}")

SpeakTest(f"WHAT DO YOU WANT TO DO {s}?")

with sr.Microphone() as source:
    try:
        print('listening...')
        voice = listener.listen(source)
        text = listener.recognize_google(voice)
        text = text.lower()
    except:
        print("TRY AGAIN")
text = text.lower()
takecommand(text)
