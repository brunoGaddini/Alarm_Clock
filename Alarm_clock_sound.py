from pygame import mixer
from tkinter import *

#cr1 = "#feffff"  # White

window = Tk()
window.title("")
window.geometry('350x150')
#window.configure(background=cr1)
window.resizable(width=False, height=False)

mixer.init() # Initializing the mixer
mixer.music.load('sound1.mp3')
mixer.music.play()

window.mainloop()