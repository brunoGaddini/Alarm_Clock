# Import Libraries
import tkinter
import PIL
import pygame
import matplotlib
import time

from tkinter.ttk import *
from tkinter import *

from PIL import Image, ImageTk

from matplotlib import image
from matplotlib.pyplot import text

from pygame import mixer

from datetime import datetime
from time import sleep

from threading import Thread #allows multiple functions to work at the same time

# Color Pallete

cr0 = "#f0f3f5"  # Black
cr1 = "#feffff"  # White
cr2 = "#d6872d"  # Gold
cr3 = "#fc766d"  # Red
cr4 = "#403d3d"  # Letter Color
cr5 = "#4a88e8"  # Blue

# Creating the Window

window = Tk()
window.title("")
window.geometry('350x150')
window.configure(background=cr1)
window.resizable(width=False, height=False)

# window.mainloop()

# Splitting the window into two frames

frame_logo = Frame(window, width=400, height=10, background=cr2)
frame_logo.grid(row=0, column=0, pady=1, padx=0)

frame_body = Frame(window, width=400, height=290, background=cr1)
frame_body.grid(row=1, column=0, pady=1, padx=0)

# Configuring the logo frame

l_line = Label(frame_logo, height=1, background=cr2, anchor=NW, font=('Ivy 1'))
l_line.place(x=0, y=0)

# Configuring the body frame

l_line = Label(frame_logo, height=1, background=cr2, anchor=NW, font=('Ivy 1'))
l_line.place(x=0, y=0)

# Configuring the image frame

imagem = Image.open(r'C:\Users\Bruno\Desktop\Python\Depertador\icon1.png')
imagem = imagem.resize((100, 100))
imagem = ImageTk.PhotoImage(imagem)

l_imagem = Label(frame_body, height=100, image=imagem, compound=LEFT, padx=10, anchor=NW, font=('Ivy 16 bold'), background=cr1, fg=cr3)  # fg = letter color
l_imagem.place(x=10, y=10)

# Configuring the name frame

l_imagem = Label(frame_body, height=100, image=imagem, compound=LEFT, padx=10, anchor=NW, font=('Ivy 16 bold'), background=cr1, fg=cr3)
l_imagem.place(x=10, y=10)

# Configuring the text frame

l_text = Label(frame_body, text='Alarme', height=1, anchor=NE, font=('Ivy 10 bold'), background=cr1, fg=cr4)  # fg = text color
l_text.place(x=127, y=10)

# Creating the combobox

# Hours
l_hours = Label(frame_body, text='Hours', height=1, anchor=NW, font=('arial 7'), background=cr1, fg=cr4)  # fg = text color
l_hours.place(x=127, y=40)
c_hour = Combobox(frame_body, width=2, font=('Ivy 15'))
c_hour['value'] = ("00", "01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12")
c_hour.current(0) # setting index order
c_hour.place(x=130, y=58)

# Minutes
l_minutes = Label(frame_body, text='Minutes', height=1, anchor=NW, font=('arial 7'), background=cr1, fg=cr4)  # fg = text color
l_minutes.place(x=177, y=40)
c_minutes = Combobox(frame_body, width=2, font=('Ivy 15'))
c_minutes['value'] = ("00", "01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21", "22", "23", "24", "25", "26", "27", "28", "29", "30", "31", "32", "33", "34", "35", "36", "37", "38", "39", "40", "41", "42", "43", "44", "45", "46", "47", "48", "49", "50", "51", "52", "53", "54", "55", "56", "57", "58", "59")
c_minutes.current(0) # setting index order
c_minutes.place(x=180, y=58)

# Seconds
l_seconds = Label(frame_body, text='Seconds', height=1, anchor=NW, font=('arial 7'), background=cr1, fg=cr4)  # fg = text color
l_seconds.place(x=227, y=40)
c_seconds = Combobox(frame_body, width=2, font=('Ivy 15'))
c_seconds['value'] = ("00", "01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21", "22", "23", "24", "25", "26", "27", "28", "29", "30", "31", "32", "33", "34", "35", "36", "37", "38", "39", "40", "41", "42", "43", "44", "45", "46", "47", "48", "49", "50", "51", "52", "53", "54", "55", "56", "57", "58", "59")
c_seconds.current(0) # setting index order
c_seconds.place(x=230, y=58)

# Period
l_period = Label(frame_body, text='Period', height=1, anchor=NW, font=('arial 7'), background=cr1, fg=cr4)  # fg = text color
l_period.place(x=277, y=40)
c_period = Combobox(frame_body, width=3, font=('Ivy 15'))
c_period['value'] = ("AM", "PM")
c_period.current(0) # setting index order
c_period.place(x=280, y=58)

# Creating the activate button

#function to indicate selected button activate alarm
def activate_alarm():
    if activate.get() ==1:
        print('Activate: ', activate.get())
    else:
        # Creating the thread
        # Allows multiple functions to work at the same time
        t1 = Thread(target=alarm)
        # Start thread
        t1.start()

# Function to deactivate the alarm
def activate_alarm():
    if activate.get() ==1:
        print('Activate: ', activate.get())
    else:
        # Creating the thread
        # Allows multiple functions to work at the same time
        t1 = Thread(target=alarm)
        # Start thread
        t1.start()

activate = IntVar()
radio = Radiobutton(frame_body, command=activate_alarm,text="Activate", value=1, variable=activate, font=('arial 8 bold'), background=cr1, fg=cr4)
radio.place(x=125, y=95)

# Inserting alarm clock sound
def ring_alarm():
    #mixer.init()  # Initializing the mixer
    mixer.music.load('sound1.mp3')
    mixer.music.play()

def alarm():
    while True:
        control = activate.get()
        h_hour = c_hour.get()
        m_minutes = c_minutes.get()
        s_seconds = c_seconds.getint()
        p_period = c_period.upper()

# Getting the current time
        current_time = datetime.now()

        hour = current_time.strftime("%I")
        minut = current_time.strftime("%M")
        second = current_time.strftime("%S")
        period = current_time.strftime("%p")

        if control==1:
            if p_period == period:
                if h_hour == hour:
                    if m_minutes == minut:
                        if s_seconds == second:
                            print("Time to take a break")
                            ring_alarm()
        sleep(1)

# Creating the thread
# Allows multiple functions to work at the same time
t1 = Thread(target=alarm)

t1.start()
mixer.init()

window.mainloop()

#https://www.youtube.com/watch?v=j4aqAS3100I