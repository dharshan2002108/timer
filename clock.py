
from tkinter import *
from tkinter.ttk import *
from time import strftime
root = Tk()
root.title("Digital Clock")
def time():
    time_string=strftime('%H:%M:%S %p')
    clock_lbl.config(text = time_string)
    clock_lbl.after(1000, time)
clock_lbl= Label(root,
                 font = ('calibri',100, 'bold'),
                 background='purple',
                 foreground='white'
                )
clock_lbl.pack(anchor = 'center')
time()
mainloop()
