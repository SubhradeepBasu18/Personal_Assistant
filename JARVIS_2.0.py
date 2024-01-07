import pyttsx3
import speech_recognition as sr
import pywhatkit
import datetime
import webbrowser
import time

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty("voices")
engine.setProperty("rate", 150)
engine.setProperty("voice", voices[0].id)


def SpeakTest(command):
    engine.say(command)
    engine.runAndWait()


def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 0.5
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language="en-in")
        print(f"User said: {query}\n")
        return query
    except Exception as e:
        print("Say that again please...")
        return None

def search(keyword):
    search_url = f"https://www.google.com/search?q={keyword}"
    webbrowser.open_new_tab(search_url)


def calculate(text):
    if "calculate" in text and "multiplied by" in text:
        # Extracting the numerical parts for multiplication
        parts = text.split("multiplied by")
        try:
            # Extract numbers and perform multiplication
            num1 = int(parts[0].replace("calculate", "").strip())
            num2 = int(parts[1].strip())
            result = num1 * num2

            SpeakTest(f"The result of {num1} multiplied by {num2} is {result}")
        except ValueError:
            SpeakTest("Please provide valid numbers for multiplication")
        except Exception as e:
            print("Error occurred:", e)
            SpeakTest("Sorry, I couldn't perform the calculation")
    elif "calculate" in text:
        operation = text.replace("calculate", "").strip()
        try:
            result = eval(operation)  # Evaluating the mathematical expression
            SpeakTest(f"The result of {operation} is {result}")
        except Exception as e:
            print("Error occurred:", e)
            SpeakTest("Sorry, I couldn't perform the calculation")

    else:
        SpeakTest("Sorry, I couldn't understand the command")


def greet_user():
    hour = datetime.datetime.now().hour
    if 0 < hour <= 12:
        SpeakTest("GOOD MORNING")
    elif 12 < hour <= 15:
        SpeakTest("GOOD AFTERNOON")
    else:
        SpeakTest("GOOD EVENING")

    SpeakTest("HELLO! I'M JARVIS, YOUR PERSONAL ASSISTANT AT YOUR SERVICE")
    # SpeakTest("CAN I KNOW YOUR NAME?")
    # name = takecommand()
    # SpeakTest(f"WELCOME {name.capitalize()}")
    name = "Bose"
    SpeakTest(f"WHAT DO YOU WANT TO DO {name.capitalize()}?")


greet_user()
k = 0
while True:
    if k != 0:
        SpeakTest("Anything else?")
    command = takecommand()
    if command:
        k = 1
        if "calculate" in command:
            print("Calculating")
            calculate(command)
        elif "play" in command:
            song = command.replace("play", "").strip()
            print("Playing...")
            SpeakTest("Playing")
            pywhatkit.playonyt(song)
        elif "exit" in command:
            print("Adios")
            SpeakTest("Adios!")
            break
        elif "search" in command:
            keyword = command.replace("search","").strip()
            print("Searching...")
            SpeakTest("Searching...")
            time.sleep(2)
            search(keyword)
        else:
            SpeakTest("I didn't understand that. Can you repeat?")
    else:
        print("No command received. Please try again.")
