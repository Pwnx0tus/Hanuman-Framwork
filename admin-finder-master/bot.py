# Import required libraries
import nltk
import os
import concurrent.futures
try:
        import requests
except ImportError:
        os.system("clear")
        os.system("pip install requests")
try:
        from colorama import *
except ImportError:
        os.system("clear")
        os.system("pip install colorama")
import time
os.system("clear")
auth = """
===================+====================
 _  __     _                   _     
| |/ /   _| |_ _   _ _ __ ___ | |__  
| ' / | | | __| | | | '_ ` _ \| '_ \ 
| . \ |_| | |_| |_| | | | | | | |_) |
|_|\_\__,_|\__|\__,_|_| |_| |_|_.__/ 
                                    
===================+====================

    Kutumb Ai Chatbot 
    Developer:TR TROJAN 
    VERSION: NOT REALEASED (Beta )
                        """

print(Style.BRIGHT)
print(Fore.GREEN+auth)
from nltk.chat.util import Chat, reflections
 # Define pattern-response pairs
pairs = [
    ['hi|hello|hey', ['Hello', 'Hey there']],
    ['what is your name?', ['My name is Kutumb, how can I help you?']],
    ['how are you?', ['I am doing well, thank you. How about you?']],
    ['i am fine', ['Glad to hear that. How can I assist you today?']],
    ['goodbye|bye|see you later', ['Goodbye, take care.']],
    ['what time is it?', ['Sorry, I am not capable of telling time at the moment.']],
    ['(.*) created you', ['I was created by Trojan']],
    ['(.*) help (.*)', ['Sure, I can assist you with %2']],
    ['Hello Baby!',['I am fine babu... What about you']],
    ['Me thik hu',['Accha thik hai.']],
]
 # Create chatbot
chatbot = Chat(pairs, reflections)
# Start conversation loop
chatbot.converse()