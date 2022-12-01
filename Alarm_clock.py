## Import Libraries
import tkinter
import PIL

from tkinter.ttk import *
from tkinter import *
from PIL import Image, ImageTk

## Color Pallete

cr0 = "#f0f3f5" ## Black
cr1 = "#feffff" ## White
cr2 = "#d6872d" ## Gold
cr3 = "#fc766d" ## Red
cr4 = "#403d3d" ## Letter Color
cr5 = "#4a88e8" ## Blue

## Creating the Window

window= Tk()
window.title("")
window.geometry('350x150')
window.configure(background=cr1)
window.resizable(width=False, height=False)

#window.mainloop()

## Splitting the window into two frames

frame_logo = Frame(window, width=400, height=10, background=cr2)
frame_logo.grid(row=0, column=0, pady=1, padx=0)

frame_body = Frame(window, width=400, height=290, background=cr3)
frame_body.grid(row=1, column=0, pady=1, padx=0)

## Configuring the logo frame

l_line = Label(frame_logo, height=1, background=cr2, anchor=NW, font=('Ivy 1'))
l_line.place(x=0, y=0)

## Configuring the body frame

l_line = Label(frame_logo, height=1, background=cr2, anchor=NW, font=('Ivy 1'))
l_line.place(x=0, y=0)

imagem = Image.open('icon1.png')
imagem = imagem.resize(100, 100)
imagem = ImageTk.PhotoImage(imagem)

frame_body = Frame(window, width=400, height=290, background=cr3)
frame_body.grid(row=1, column=0, pady=1, padx=0)

window.mainloop()
