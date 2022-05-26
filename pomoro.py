from threading import Timer
from tkinter import *
from tkinter import ttk
import time as Time, datetime
import math

class counter():
    
    def __init__(self):
        self.root = Tk()
        self.ttl_seconds = 0
        self.running = True
        self.frm = Tk.grid(self.root)
        self.label = ttk.Label(self.root, text= self.ttl_seconds,font = 'Arial 40 bold', foreground= 'red')
        self.label.grid(column=0 , row=0)
        self.startbutton = ttk.Button(self.frm, text="Start", command=self.startPomo)
        self.startbutton.grid(column=0, row=1)
        self.quitbutton = ttk.Button(self.frm, text='Quit', command=self.quit).grid(column=1, row = 1)
    
        self.root.geometry("250x90")
        self.root.title("Pomodoro")
        self.frame = ttk.Frame(self.root, padding =0)
        self.root.mainloop()

    def startPomo(self):
        self.running = True
        self.ttl_seconds = 1500
        self.startbutton.configure(text="Stop", command=self.stopPomo)
        while self.running == 1:
            timer = "{minutes}:{seconds}".format(minutes = math.trunc(self.ttl_seconds / 60), seconds = self.ttl_seconds % 60)
            self.label.configure(text=timer)
            self.root.update()
            self.root.after(1000)
            self.ttl_seconds -= 1
    

    def quit(self):
        self.root.destroy()



    def stopPomo(self):
        self.running = False
        self.ttl_seconds = 0
        self.startbutton.configure(text="Start", command=self.startPomo)
        



app = counter()


