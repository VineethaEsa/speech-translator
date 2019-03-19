from tkinter import *

import win32com.client as wincl

import speech_recognition as sr  

import os

import tkinter as tk

root = tk.Tk()
root.title('SELECT LANGUAGE')
v = tk.IntVar()
v.set(0)  # initializing the choice, i.e. Python

languages = [
    ("French"),
    ("Spanish"),
    ("German"),
    ("Hindi"),
    ("Japanese")
]


l=["French","spanish","german","Hindi","Japanese"]
l_code=["fr-FR","es-AR","de-DE","hi-IN","ja-JP"]
    


def ShowChoice():
    print("you have selected",l[v.get()],"language successfully")

tk.Label(root, 
         text="""Choose your language:""",
         justify = tk.LEFT,
         padx = 20).pack()

for val, language in enumerate(languages):
    tk.Radiobutton(root, 
                  text=language,
                  indicatoron = 0,
                  width = 20,
                  padx = 20, 
                  variable=v, 
                  command=ShowChoice,
                  value=val).pack(anchor=tk.W)


root.mainloop()

lang = l_code[v.get()]



# get audio from the microphone                                                                       
r = sr.Recognizer()                                                                                   
with sr.Microphone() as source:                                                                       
    #lang = input()
    print("Speak:")                                                                                   
    audio = r.listen(source) 

try:
    stt = r.recognize_google(audio,language = lang)

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
out = "you spoke "+a['translation']

print(out)
e1 = Entry(master)
e2 = Entry(master)
e1.insert(10,stt)
e2.insert(40,out)

e1.grid(row=0, column=1)
e2.grid(row=1, column=1)


speak = wincl.Dispatch("SAPI.SpVoice")

speak.Speak(out)
print(a)
mainloop( )

