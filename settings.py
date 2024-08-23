from tkinter import *

def open_sets_win(root):
    top = Toplevel(root)
    top.title("Key settings menu")
    top.geometry("400x300")

    btns_frame = Frame(top)
    btns_frame.pack(side='left', anchor='n')

    A_entry = Entry(btns_frame, width=10)
    A_entry.pack(anchor='w')

    B_entry = Entry(btns_frame, width=10)
    B_entry.pack(anchor='w')

    X_entry = Entry(btns_frame, width=10)
    X_entry.pack(anchor='w')

    Y_entry = Entry(btns_frame, width=10)
    Y_entry.pack(anchor='w')

    triggers_frame = Frame(top)
    triggers_frame.pack(side='left', anchor='n', padx=5)

    LB_entry = Entry(triggers_frame, width=10)
    LB_entry.pack(side='top', anchor='e')

    RB_entry = Entry(triggers_frame, width=10)
    RB_entry.pack(side='top', anchor='e')

    LT_entry = Entry(triggers_frame, width=10)
    LT_entry.pack(side='top', anchor='e')

    RT_entry = Entry(triggers_frame, width=10)
    RT_entry.pack(side='top', anchor='e')

    top.mainloop()