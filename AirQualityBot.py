import requests
from bs4 import BeautifulSoup
import pyperclip

URL = 'https://air-quality.com/place/canada/victoria/1757c782'
headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; rv:78.0) Gecko/20100101 Firefox/78.0'}

#Scrape entire web page
page = requests.get(URL, headers=headers)
soup = BeautifulSoup(page.content, 'html.parser')

#Cut out the Index Value
index = soup.find(class_="indexValue")
IndexValue = index.string.strip('<div class="indexValue">')

#Cut out the Health Level
level = soup.find(class_="level")
HealthLevel = level.string.strip('<div class="level"')


Last = open("Discord.txt", "r")
OldIndexValue = Last.read()

#Figure out whether it went Down, Up or Same
if IndexValue == OldIndexValue:
    Variation = "constant at"
elif IndexValue > OldIndexValue:
    Variation = "increasing from"
elif IndexValue < OldIndexValue:
    Variation = "decreasing from"


print('The current Air Quality Index reading for Victoria is ' + IndexValue + ', rated ' + HealthLevel + ', ' + Variation + ' ' + OldIndexValue + ' since the last time this command was used.')

#Copy the output to clipboard
pyperclip.copy('The current Air Quality Index reading for Victoria is ' + IndexValue + ', rated ' + HealthLevel + ', ' + Variation + ' ' + OldIndexValue + ' since the last time this command was used.')

#Save previous Index Value
f = open("Discord.txt", "w")
f.write(IndexValue)
f.close()
