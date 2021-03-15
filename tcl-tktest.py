from tkinter import *

window = Tk()
window.title("Welcome to My Progam")
window.geometry('400x300')
lbl = Label(window, text="Folder to check")
lbl.grid(column=0, row=0)
txt = Entry(window,width=15)
txt.grid(column=1, row=0) 

def clicked():
    res = "Welcome to " + txt.get()
    lbl.configure(text= res)
btn = Button(window, text="search", command=clicked)
btn.grid(column=2, row=0)
window.mainloop()