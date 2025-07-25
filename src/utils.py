import datetime
import requests
from src.speech import speak

def wish_user():
    hour = datetime.datetime.now().hour
    if hour < 12:
        speak("Good Morning!")
    elif hour < 18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")
    speak("I am AI Redant. Please tell me how may I help you.")

def check_internet():
    try:
        requests.get("https://www.geeksforgeeks.org/", timeout=5)
        return True
    except requests.ConnectionError:
        return False
