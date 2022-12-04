import time

from pygame import mixer
from datetime import datetime
from tkinter import *

#cr1 = "#feffff"  # White

window = Tk()
window.title("")
window.geometry('350x150')
#window.configure(background=cr1)
window.resizable(width=False, height=False)

def play_alarm():
    mixer.init()  # Initializing the mixer
    mixer.music.load('sound1.mp3')
    mixer.music.play()

def alarm():
    while True:
        control = 1
        c_hour = "00"
        c_minutes = "30"
        c_seconds = "00"
        c_period = "am".upper()

        current_time = datetime.now()

        hour = current_time.strftime("%I")
        minut = current_time.strftime("%M")
        second = current_time.strftime("%S")
        period = current_time.strftime("%p")


window.mainloop()