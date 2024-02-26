import tkinter as tk
from gtts import gTTS
import os

def speak_text():
  text = entry.get()
  language = "en"  
  tts = gTTS(text=text, lang=language, slow=False)
  tts.save("result.mp3")
  os.system("afterplay output.mp3") 


root = tk.Tk()
root.title("Text to Speech")


label = tk.Label(root, text="Enter a text to speak:")
label.pack()

entry = tk.Entry(root, width=50)
entry.pack()

speak_button = tk.Button(root, text="Speak", command=speak_text)
speak_button.pack()



root.mainloop()






