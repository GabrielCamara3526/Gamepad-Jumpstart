from tkinter import *
from random import choice
vowels = ["a","e","i","o","u"]

def update_b():
    b1.configure(text=b2.cget("text"))
    b2.configure(text=choice(vowels))



win = Tk()
win.geometry("250x250")

b1 = Button(win, height=5, width=5, text=choice(vowels), font=('Roboto', 20), command=update_b)
b1.grid(row=3, column=0)

b2 = Button(win, height=5, width=5, text=choice(vowels), font=('Roboto', 20))
b2.grid(row=3, column=1)

win.mainloop()
