import speech_recognition as sr
from time import ctime
import time
import os
from gtts import gTTS
from test_speaker import speakerName
from sound import saveAudio
from lxml import html
import requests
import webbrowser
import subprocess  
import warnings
warnings.filterwarnings("ignore")

mlist=[]

def speak(audioString):
    print(audioString)
    tts = gTTS(text=audioString, lang='en')
    tts.save("audio.mp3")
 
def recordAudio():
    # Record Audio
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Which app would you like to open?")
        audio = r.listen(source)
 
    # Speech recognition using Google Speech Recognition
    data = ""
    try:
        data = r.recognize_google(audio)
        print("You said: " + data+"\n")
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))
 
    return data
 
def jarvis(t):
    if "how are you" in t:
        speak("I am fine")
 
    if "what time is it" in t:
        speak(ctime())

    if(t.find("open")!=-1):                                                   # Open windows application
        le=t.find("open")+len("open")+1
        t=t[le:]
        if(t=="calculator" or t=="Calculator"):
            os.system("start calc.exe")
        elif(t=="Notepad" or t=="notepad"):
            os.system("start notepad.exe")
        elif(t=="Paint" or t=="paint"):
            os.system("start mspaint.exe")
        elif((t.find("Chrome")!=-1) or (t.find("chrome")!=-1) or (t.find("Browser")!=-1) or (t.find("browser")!=-1)):
            subprocess.Popen([r"C:\Users\Amitansh Gangwar\AppData\Local\Google\Chrome\Application\chrome.exe"])           
        elif((t=="firefox" or t=="Firefox" or t=="fire fox" or t=="Fire Fox")):
            subprocess.Popen([r"C:\Program Files (x86)\Mozilla Firefox\firefox.exe"])
        elif((t=="Adobe Reader" or t=="Adobe reader" or t=="adobe reader" or t=="adobe Reader")):
            subprocess.Popen([r"C:\Program Files (x86)\Adobe\Reader 11.0\Reader\AcroRd32.exe"])
        elif(t=="Picasa" or t=="picasa"):
            subprocess.Popen([r"C:\Program Files (x86)\Google\Picasa3\Picasa3.exe"])  
        elif((t=="ShareIt" or t=="shareit" or t=="Shareit" or t=="sharesIt")):
            subprocess.Popen([r"C:\Program Files (x86)\SHAREit Technologies\SHAREit\SHAREit.exe"])
        elif(t=="dictionary" or t=="Dictionary"):
            subprocess.Popen([r"C:\Program Files (x86)\PublicSoft\EngDict\Dictionary.EXE"])
        elif(t=="word" or t=="Word"):
            subprocess.Popen([r"C:\Program Files (x86)\Microsoft Office\root\Office16\WINWORD.EXE"])
        elif(t=="music player" or t=="Music player" or t=="Music Player" or t=="music Player"):
            subprocess.Popen([r"C:\Program Files (x86)\Windows Media Player\wmplayer.exe"])
        elif(t=="video player" or t=="Video player" or t=="video Player" or t=="Video Player"):
            subprocess.Popen([r"C:\Program Files (x86)\CyberLink\PowerDVD14\PDVDLP.exe"])
 
def validate():
    saveAudio()
    users=["Amitansh1","Sandeep"]
    name=speakerName()
    if name in users:
        return name
    else:
        return "not_found"

#initialization
print("Speak the pass phrase:\n")
val=validate()
while(val=="not_found"):
    print ("Not recognized\n")
    val=validate()

print("\n")
print("Hi ")
print(val+'\n')
#print("What can I do for you?")
while 1:
    data = recordAudio()
    jarvis(data)
