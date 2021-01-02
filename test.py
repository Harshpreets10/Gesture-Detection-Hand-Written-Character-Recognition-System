from gtts import gTTS
from pygame import mixer  # Load the popular external library
#from mpyg321.mpyg321 import MPyg321Player
from io import BytesIO
#import vlc
import playsound


import os
text='hey'
lang='en'
obj=gTTS(text=text,lang='en',slow=False)
obj.save("welcome.mp3")
playsound.playsound(r'C:\Users\EZIO\Desktop\translator minor\welcome.mp3', True)

#player=MPyg321Player()
#player.play_song("welcome.mp3")



