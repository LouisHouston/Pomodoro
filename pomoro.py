from threading import Timer
from tkinter import *
from tkinter import ttk
import time as Time, datetime
import platform

class counter():
    
    def __init__(self):
        self.root = Tk()
        self.label = Tk.Label(self.root, text = "Text")
        self.ttl_seconds = 0
        self.frm = Tk.grid()
        self.startbutton = Tk.Button(self.frm, text="Start", command=self.startPomo).grid(column=1, row=0)
        self.quitbutton = Tk.Button(self.frm, text='Quit', command=self.quit).grid(column=2, row = 0)
      
        self.root.geometry("250x70")
        self.root.title("Pomodoro")
        self.frame = ttk.Frame(self.root, padding =10)
        self.root.mainloop

    def startPomo(self):
        self.ttl_seconds = 1500
        while self.ttl_seconds > 0:
            timer = datetime.timedelta(seconds = self.ttl_seconds)
            root.update()
            root.after(1000)
            print('something')
            self.ttl_seconds -= 1
            (self.ttl_seconds)
    
    def quit(self):
        self.root.destroy()

  
            

    def stopPomo():
        ttl_seconds = 25 * 60
        



#root = Tk()
#root.geometry("250x70")
#root.title('Pomodoro')
#frm = ttk.Frame(root, padding=10 )
#pomod = counter()
#
#
#frm.grid()
#ttk.Label(frm, text= pomod.ttl_seconds,font = 'Arial 40 bold', foreground= 'cyan').grid(column=0 , row=0)
#ttk.Button(frm, text="Start", command=pomod.startPomo).grid(column=1, row=0)
#ttk.Button(frm, text='Quit', command=root.destroy).grid(column=2, row = 0)
#

app = counter()


