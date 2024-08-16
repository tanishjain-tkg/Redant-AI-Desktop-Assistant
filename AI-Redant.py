from tkinter import *
from PIL import ImageTk, Image
import pyttsx3 #pip install pyttsx3
import speech_recognition as sr #pip install speechRecognition
import webbrowser
import wikipedia
import datetime
import os

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[0].id)

root=Tk()
root.title("! WELCOME TO AIREDANT !")
Label(text="HI USER! HOW MAY I HELP YOU ?",font="Arial 25 bold",bg="light blue").pack()
image=Image.open("d:\\ai desktop\\Untitled.jpg")
photo=ImageTk.PhotoImage(image)
Label(image=photo).pack()

def start():

    def speak(audio):
       engine.say(audio)
       engine.runAndWait()

    def wishMe():
        hour = int(datetime.datetime.now().hour)
        if hour>=0 and hour<12:
            speak("Good Morning!")
            print("Good Morning!")

        elif hour>=12 and hour<18:
            speak("Good Afternoon!")
            print("Good Afternoon!")  

        else:
            speak("Good Evening!")
            print("Good Evening!") 
        speak("I am AI Redant. Please tell me how may I help you")
        print("I am AI Redant. Please tell me how may I help you")
        
        def internet_connection():
            try:
                response= requests.get("https://www.geeksforgeeks.org/",timeout=5)
                return True
            except requests.ConnectionError:
                return False
        if internet_connection():
            print("THE INTERNET IS CONNECTED !")
            speak("THE INTERNET IS CONNECTED !")
        else:
            print("THE INTERNET IS NOT CONNECTED !")
            speak("THE INTERNET IS NOT CONNECTED !")      
    
    def takeCommand():
       
       r = sr.Recognizer()
       with sr.Microphone() as source:
           print("Listening...")
           r.pause_threshold = 1
           audio = r.listen(source,timeout=8,phrase_time_limit=8)
       
       try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")
       
       except Exception as e:    
        print(" Sorry Say that again please...")
        speak("Sorry say that again please...")  
        return "None"
       
       return query
    
    if __name__ == "__main__":
       wishMe()
       while True:
       #if 1:
        
        query = takeCommand().lower()

        # Logic for executing tasks based on query

        if 'open youtube' in query:
            webbrowser.open("youtube.com")
        
        elif 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open mail' in query:
            webbrowser.open("gmail.com")

        elif 'joke' in query:
            print(pyjokes.get_joke())
            speak(pyjokes.get_joke()) 

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")   

        elif 'time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f" The time is {strTime}")

        elif 'exit' in query:
            print("Thank You! See you soon!")
            speak("Thank You! See you soon!")
            break

Button(bg="white",fg="black",text="START",font="Arial 15 bold",relief="sunken",borderwidth=5,command=start).pack()

root.mainloop()