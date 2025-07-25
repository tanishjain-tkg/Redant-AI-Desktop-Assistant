from tkinter import *
from PIL import ImageTk, Image
from src.assistant import run_assistant

def launch_gui():
    root = Tk()
    root.title("! WELCOME TO AIREDANT !")

    Label(text="HI USER! HOW MAY I HELP YOU ?", font="Arial 25 bold", bg="light blue").pack()
    image = Image.open("assets/logo.jpg")  # Use your image name
    photo = ImageTk.PhotoImage(image)
    Label(image=photo).pack()

    Button(
        bg="white",
        fg="black",
        text="START",
        font="Arial 15 bold",
        relief="sunken",
        borderwidth=5,
        command=lambda: run_assistant(root)
    ).pack()

    root.mainloop()
    