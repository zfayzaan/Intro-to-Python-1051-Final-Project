from tkinter import *
import subprocess

ws = Tk()
ws.geometry('1000x800')
ws.title('PythonGuides')
ws['bg']='#5d8a82'

f = ("Times bold", 14)

def clicker():
    ws.destroy()
    import clicker

def mapSelect():
    ws.destroy()
    import map_select
def aboutUs():
    ws.destroy()
    import aboutUs
Label(
    ws,
    text="Cookie Clicker Game",
    padx=20,
    pady=20,
    bg='#990014',
    font=f
).pack(expand=True, fill=BOTH)

Button(
    ws, 
    text="Select Map", 
    font=f,
    command=mapSelect
    ).pack(fill=X, expand=TRUE, side=LEFT)

Button(
    ws, 
    text="Play Game",
    font=f,
    command=clicker
    ).pack(fill=X, expand=TRUE, side=LEFT)
    
ws.mainloop()
subprocess.call(["afplay", "clicksound.wav"])
