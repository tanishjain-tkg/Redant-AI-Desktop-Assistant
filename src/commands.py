import webbrowser
import wikipedia
import datetime
import pyjokes
from src.speech import speak

def handle_query(query):
    if 'open youtube' in query:
        webbrowser.open("https://youtube.com")
        return True

    elif 'open google' in query:
        webbrowser.open("https://google.com")
        return True

    elif 'open mail' in query:
        webbrowser.open("https://gmail.com")
        return True

    elif 'open stackoverflow' in query:
        webbrowser.open("https://stackoverflow.com")
        return True

    elif 'joke' in query:
        joke = pyjokes.get_joke()
        print(joke)
        speak(joke)
        return True

    elif 'time' in query:
        strTime = datetime.datetime.now().strftime("%H:%M:%S")
        speak(f"The time is {strTime}")
        return True

    elif 'wikipedia' in query:
        speak('Searching Wikipedia...')
        try:
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)
        except Exception:
            speak("Sorry, couldn't fetch from Wikipedia.")
        return True

    return False  # Unhandled command
