import requests
import bs4
import os
import concurrent.futures
try:
  import requests
  import requests
except ImportError:
  os.system("clear")
  os.system("pip install requests")
  os.system("clear")
  os.system("pip install requests")
try:
  from colorama import *
  from colorama import *
except ImportError:
  os.system("clear")
  os.system("pip install colorama")
  os.system("clear")
  os.system("pip install colorama")
import time


os.system("clear")
auth = """

=================+===================
| |/ /   _| |_ _   _ _ __ ___ | |__  
| ' / | | | __| | | | '_ ` _ \| '_ \ 
| . \ |_| | |_| |_| | | | | | | |_) |
|_|\_\__,_|\__|\__,_|_| |_| |_|_.__/ 
=================+===================
    Kutumb Url Extractor 
    TEAM: TROEXHACK SECURITY & SHELL SQUAD
    Developer:Gandharv
    VERSION:0.5 BETA
                        """

print(Style.BRIGHT)
print(Fore.GREEN + auth)


print(Fore.GREEN + auth)


def extract_urls(url):
    try:
        response = requests.get(url)
        soup = bs4.BeautifulSoup(response.text, 'html.parser')
        hrefs = []
        img_links = []
        meta_tags = []
        # Find all <a>, <img>, and <meta> tags:
        for tag in soup.find_all(['a', 'img', 'meta']):
            # Extract the URL, if it exists:
            if tag.has_attr('href'):
                hrefs.append(tag['href'])
            elif tag.has_attr('src'):
                img_links.append(tag['src'])
            elif tag.has_attr('content'):
                meta_tags.append(tag['content'])
        return hrefs, img_links, meta_tags
    except:
        print("An error occurred while extracting URLs.")
        return [], [], []

# Prompt the user for a website URL:
url = input("Enter a website URL: ")

# Extract URLs from the webpage:
hrefs, img_links, meta_tags = extract_urls(url)

# Print the URLs for each section:
print("Found {} standard links:".format(len(hrefs)))
for url in hrefs:
    print(url)

print("\nFound {} image links:".format(len(img_links)))
for link in img_links:
    print(link)

print("\nFound {} meta tags:".format(len(meta_tags)))
for tag in meta_tags:
    print(tag)