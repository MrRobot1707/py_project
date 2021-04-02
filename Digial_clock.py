from  tkinter import *
import time

main = Tk()
main.title("Digital clock")
main.geometry('580x150')
main.resizable(0,0)

text_font = ('Boulder',68,'bold')
background = '#FFFF00'
foreground = '#000000'

border_width = 25

label = Label(main,font=text_font, bg=background, fg=foreground, bd=border_width)
label.grid(row=0,column=1)

def Digitel_clock():
	curren_time = time.strftime("%H:%M:%S %p")
	label.config(text=curren_time)
	label.after(200,Digitel_clock)

Digitel_clock()
main.mainloop()