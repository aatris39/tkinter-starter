# A starter program for Python with Tkinter

from tkinter import * # import Tkinter library
from tkinter.ttk import *
from ttkthemes import ThemedTk


window = ThemedTk(theme = "arc")         # Create the application window
window.title("Hello")
window.geometry('500x500')

combo = Combobox(window)
combo['values']= (1, 2, 3, 4, 5, "Text")
combo.current(1) #set the selected item
combo.grid(column=0, row=0)

lbl = Label(window, text="Welcome", font=("Arial Bold",10))
lbl.grid(column=0, row=0)

txt = Entry(window, width=10)
txt.grid(column=1, row=0)


def clicked():
    lbl.configure(text=txt.get() +" clicked the button!")
    lbl.configure(text=res)
    
txt.focus()

btn = Button(window, text="Click Me", command=clicked)
btn.grid(column=2, row=0)



window.mainloop() # Keep the window open



