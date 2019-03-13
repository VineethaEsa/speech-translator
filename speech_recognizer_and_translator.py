from tkinter import *

import win32com.client as wincl

import speech_recognition as sr  

import os

# get audio from the microphone                                                                       
r = sr.Recognizer()                                                                                   
with sr.Microphone() as source:                                                                       
    print("Speak:")                                                                                   
    audio = r.listen(source) 

try:
    stt = r.recognize_google(audio,language = "fr_FR")

except sr.UnknownValueError:
    print("Could not understand audio")

except sr.RequestError as e:
    print("Could not request results; {0}".format(e))



import Algorithmia

input = {
  "action": "translate",
  "text": stt
}
client = Algorithmia.client('simYKU0YVtXsbRlb6Tp9K4IKVwL1')
algo = client.algo('translation/GoogleTranslate/0.1.1')
algo.set_options(timeout=300) # optional

    
master = Tk()
Label(master, text="Input").grid(row=0)
Label(master, text="Output").grid(row=1)

a = algo.pipe(input).result

e1 = Entry(master)
e2 = Entry(master)
e1.insert(10,stt)
e2.insert(40,a)

e1.grid(row=0, column=1)
e2.grid(row=1, column=1)


speak = wincl.Dispatch("SAPI.SpVoice")

speak.Speak(a)

mainloop( )
