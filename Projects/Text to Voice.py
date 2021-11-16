from gtts import gTTS
import os

mytext = "Welcome to my world and my name is jhon cena and you cant see me"
language = "en"
myobj = gTTS(text=mytext, lang=language, slow=False)
myobj.save("Welcome.mp3")
os.system("Welcome.mp3")