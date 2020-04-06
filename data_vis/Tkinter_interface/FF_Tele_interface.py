import sys
import SerialRead

import time
import threading

from tkinter import *
#import tkinter		# not needed 
#from tkinter import ttk

from PIL import Image, ImageTk
from playsound import playsound
from pygame import mixer  # Load the popular external library

import matplotlib
matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib.figure import Figure

#import serial
#from serial.tools import list_ports
#from serial import tools

window = Tk()
window.configure(background='black')
window.title("Fuel Fighters cool interface")
window.geometry('1000x600')


x_var = []
y_var = []

buffArray = []
baudrate = 9600
arrLen = 128
packCount = 0
#print(list_ports.comports())


#INITIALIZING SERIAL. 
# this is now imported from SerialRead.py to make it more readable
# change 'COM4' to 'dev..' whatever for linux
ser = SerialRead.SerialRead('COM4', baudrate, arrLen)

ser.readSerialToArray(ser, buffArray, arrLen, packCount)

mixer.init()
#mixer.music.load('song.mp3')
#mixer.music.play()


# make a scrollbar
# maybe unnecessary
scrollbar = Scrollbar(window)
scrollbar.pack(side=RIGHT, fill=Y)


load = Image.open("dnvglFFlogo.png")
render = ImageTk.PhotoImage(load)
panel =Label(window, image = render)
panel.pack(side = "top", fill = "both", expand = "yes")


# make a text box to put the serial output
log = Text (window, width=10, height=30, takefocus=0)
log.pack(side="left",fill="y")


# attach text box to scrollbar
log.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=log.xview)


lbl=Label(window, text="Fuel Fighters new interface",font=("Arial Bold", 18))
#lbl.grid(column=0, row=0)
lbl.pack(side = "top", fill = "both", expand = "yes")


#lbl2=Label(window,font=("Arial Bold", 12))
#lbl2.grid(column=0, row=2)
#lbl2.pack(side = "left", fill = "both", expand = "yes")

#lbl3=Label(window,text="Enter your name",font=("Arial Bold", 12))
#lbl3.grid(column=1, row=2)
#lbl3.pack(side = "right", fill = "both", expand = "yes")

#txt = Entry(window,width=10)
#txt.grid(column=1, row=3)
#txt.focus()
#txt.pack(side = "right", fill = "both", expand = "yes")



def clicked():
	#res = "Hello " + txt.get()
	#lbl2.configure(text= res)
	#lbl2.configure(text="Button was clicked !!")
	if ser.inWaiting():
		#print("here")
		data_serial = ser.readline()
		reads = float(data_serial)
		#print(data_serial)
		#lbl2.configure(text= data_serial)
		log.insert('0.0', reads)
		log.insert('0.0', '\n')
		x_var.append(time.time())
		y_var.append(float(data_serial))
		a.plot(x_var,y_var)#[1,2,3,4,5,6,7,8],[5,6,1,3,8,9,3,5])
		canvas.show()
		toolbar.update()
		window.after(1000, clicked)


def close():
	window.destroy()


def pause():
	mixer.music.pause()
	#playsound('song.mp3')


def unpause():
	mixer.music.unpause()


btn = Button(window, text="Click Me", command=clicked,bg="gray", fg="blue")
#btn = Button(window, text="Click Me",bg="gray", fg="blue")
#btn.grid(column=0, row=1)
btn.pack(side = "left", fill = "both", expand = "yes")


btn2 = Button(window, text="Quit", command=close,bg="white", fg="black")
btn2.pack(side = "left", fill = "y", expand = "no")


btn3 = Button(window, text="pause", command=pause,bg="white", fg="black")
btn3.pack(side = "right", fill = "both", expand = "yes")


btn4 = Button(window, text="unpause", command=unpause,bg="white", fg="black")
btn4.pack(side = "right", fill = "both", expand = "yes")


f = Figure(figsize=(5,5), dpi=100)
a = f.add_subplot(111)
canvas = FigureCanvasTkAgg(f, window)
canvas.get_tk_widget().pack(side=BOTTOM, fill=Y, expand=False)


toolbar = NavigationToolbar2Tk(canvas, window)
canvas._tkcanvas.pack(side=BOTTOM, fill=Y, expand=False)


window.mainloop()

