from src.speech import speak, take_command
from src.utils import check_internet, wish_user
from src.commands import handle_query
import random

def run_assistant(root):
    wish_user()
    if check_internet():
        speak("The internet is connected.")
    else:
        speak("The internet is not connected.")

    while True:
        query = take_command().lower()

        if query == "none":
            continue

        if 'exit' in query:
            speak("Thank you. See you soon.")
            root.quit()
            break

        handled = handle_query(query)
        if not handled:
            fallback_responses = [
                "I'm still learning. Could you rephrase that?",
                "That sounds interesting, but I can't do that yet.",
                "Maybe I’ll learn that soon.",
                "I'm not sure how to help with that.",
                "That's beyond my capabilities at the moment."
            ]
            response = random.choice(fallback_responses)
            print(f"Fallback: {response}")
            speak(response)
