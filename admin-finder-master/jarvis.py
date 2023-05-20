import speech_recognition as sr 
import pyttsx3 
import datetime 
import webbrowser 
import os 
import random 
 # Initialize speech recognition engine
r = sr.Recognizer()
 # Initialize text-to-speech engine
engine = pyttsx3.init()
 # Set speech rate
engine.setProperty('rate', 180)
 # Jarvis introduction
engine.say("Hello. I am Jarvis, your personal assistant.")
engine.say("What can I do for you today?")
engine.runAndWait()
 # Main function to listen for commands
def listen():
    with sr.Microphone() as source:
        print("Listening...")
        audio_data = r.listen(source)
        print("Recognizing...")
        # Convert speech to text using Google Speech Recognition
        command = r.recognize_google(audio_data)
        print("You said: ", command)
        return command.lower()
 # Main program loop
while True:
    # Get command from user
    command = listen()
     # Process command
    if "hello" in command or "hi" in command:
        # Greet user
        engine.say("Hello. How can I help you?")
        engine.runAndWait()
    elif "what is the time" in command or "tell me the time" in command:
        # Get current time
        now = datetime.datetime.now().strftime("%I:%M %p")
        # Speak time
        engine.say("The time is " + now)
        engine.runAndWait()
    elif "search" in command:
        # Remove 'search' from command
        command = command.replace("search", "")
        # Open search results in default web browser
        webbrowser.open("https://www.google.com/search?q=" + command)
        engine.say("Here are the search results for " + command)
        engine.runAndWait()
    elif "open" in command:
        # Remove 'open' from command
        command = command.replace("open", "")
        # Open application or website
        if "google" in command:
            webbrowser.get().open_new_tab("https://www.google.com")
            engine.say("Google has been opened")
            engine.runAndWait()
        elif "youtube" in command:
            webbrowser.get().open_new_tab("https://www.youtube.com")
            engine.say("Youtube has been opened")
            engine.runAndWait()
        elif "gmail" in command:
            webbrowser.get().open_new_tab("https://www.gmail.com")
            engine.say("Gmail has been opened")
            engine.runAndWait()
        # Open file explorer
        elif "file explorer" in command:
            os.startfile('explorer.exe')
            engine.say("File explorer has been opened")
            engine.runAndWait()
    elif "tell me a joke" in command:
        # Tell a joke
        jokes = ["Why did the tomato turn red? Because it saw the salad dressing!", 
                 "Why was the math book sad? Because it had too many problems", 
                 "Why can't you hear a pterodactyl go to the bathroom? Because the pee is silent."]
        joke = random.choice(jokes)
        engine.say(joke)
        engine.runAndWait()
    elif "exit" in command or "bye" in command:
        # Exit program loop
        engine.say("Goodbye")
        engine.runAndWait()
        break
    else:
        # Give error message if command not recognized
        engine.say("I'm sorry, I don't understand. Please try again.")
        engine.runAndWait()