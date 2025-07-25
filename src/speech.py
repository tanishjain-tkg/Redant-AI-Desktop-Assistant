import pyttsx3
import speech_recognition as sr

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def speak(text):
    engine.say(text)
    engine.runAndWait()

def take_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 3
        try:
            audio = r.listen(source, timeout=8, phrase_time_limit=8)
        except sr.WaitTimeoutError:
            print("Listening timed out.")
            speak("I didn't hear anything. Please try again.")
            return "none"

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}")
    except Exception:
        print("Sorry, say that again please...")
        speak("Sorry, say that again please...")
        return "none"

    return query
