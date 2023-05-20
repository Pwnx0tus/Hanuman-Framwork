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
_   _    _    _   _ _   _ __  __    _    _   _ 
| | | |  / \  | \ | | | | |  \/  |  / \  | \ | |
| |_| | / _ \ |  \| | | | | |\/| | / _ \ |  \| |
|  _  |/ ___ \| |\  | |_| | |  | |/ ___ \| |\  |
|_| |_/_/   \_\_| \_|\___/|_|  |_/_/   \_\_| \_|

    HANUMAN Framework Bug Hunting GOD Tool
    Team:TROEXHACK SECURITY & SHELL SQUAD
    Developer:Gandharv
    VERSION:0.5 BETA
                        """

print(Style.BRIGHT)
print(Fore.GREEN+auth)
# define the file paths for each option
option_1_file = "sqlmap.py"
option_2_file = "XSStrike-master/xsstrike.py"
option_3_file = "PwnXSS/pwnxss.py"
option_4_file = "admin-finder-master/admin-finder.py"
option_5_file = "Kutumb-Url-Extractor/Kutumb.py"
# display the menu options
print("Select an options:")
print("[*] Sqlmap   [1]")
print("[*] XSStrike [2]")
print("[*] PwnXss   [3]")
print("[*] Admin Finder [4]")
print("[*] Url Extractor [5]")


# get the user's choice
choice = input("Enter your choice (1, 2, 3 ,4 or 5.): ")

# run the selected file
if choice == "1":
    os.system("python " + option_1_file)
elif choice == "2":
    os.system("python " + option_2_file)
elif choice == "3":
    os.system("python " + option_3_file)
elif choice == "4":
    os.system("python " + option_4_file)
elif choice == "5":
    os.system("python " + option_5_file)
else:
    print("Invalid choice. Please enter 1, 2, 3, 4 or 5.")
