from tkinter import *
from game_tiles import app_bg_theme
from root_window import a_var, b_var, x_var, y_var
from root_window import  rb_var, lb_var, rt_var, lt_var

def open_sets_win(root, event):
    
    def reset_keys():
        a_var.set('l')
        b_var.set('=')
        x_var.set('k')
        y_var.set('o')
        rb_var.set('i')
        lb_var.set('e')
        rt_var.set('p')
        lt_var.set('q')

    def save_keys():
        top.destroy()

    #Dedicate the space above to inner functions of the topLevel window under here.
    top = Toplevel(root)
    top.title("Key settings menu")
    top.geometry("400x300")
    top.resizable(False, False)
    top.configure(bg=app_bg_theme)

    global a_var, x_var, b_var, y_var
    global lb_var, rt_var, lt_var, rb_var

    entry_font = ('Roboto', 16)
    label_font = ('Roboto', 14)
    
    #These are the Button Labels
    btns_frame = Frame(top, bg=app_bg_theme)
    btns_frame.pack(side='left', anchor='n')

    A_label = Label(btns_frame, text='A: ', font=label_font, bg='lightgreen', fg='black')
    A_label.grid(row=0, column=0)

    B_label = Label(btns_frame, text='B: ', font=label_font, bg='red', fg='white')
    B_label.grid(row=1, column=0)

    X_label = Label(btns_frame, text='X: ', font=label_font, bg='blue', fg='white')
    X_label.grid(row=2, column=0)

    Y_label = Label(btns_frame, text='Y: ', font=label_font, bg='yellow')
    Y_label.grid(row=3, column=0)

    #These are the Button Entries
    A_entry = Entry(btns_frame, width=10, textvariable=a_var, font=entry_font)
    A_entry.grid(row=0, column=1)

    B_entry = Entry(btns_frame, width=10, textvariable=b_var, font=entry_font)
    B_entry.grid(row=1, column=1)

    X_entry = Entry(btns_frame, width=10, textvariable=x_var, font=entry_font)
    X_entry.grid(row=2, column=1)

    Y_entry = Entry(btns_frame, width=10, textvariable=y_var, font=entry_font)
    Y_entry.grid(row=3, column=1)

    #Button to reset all Entries
    reset_bindings = Button(btns_frame, text="Reset all", font=label_font, bg='black', fg='white', activebackground='#444444', 
                            activeforeground='white', command=reset_keys)
    reset_bindings.grid(row=4, column=0, columnspan=2, pady=10)

    #These are the trigger Labels
    triggers_frame = Frame(top, bg=app_bg_theme)
    triggers_frame.pack(side='left', anchor='n', padx=5)

    LB_label = Label(triggers_frame, text='LB: ', font=label_font, bg='black', fg='white')
    LB_label.grid(row=0, column=0)

    RB_label = Label(triggers_frame, text='RB: ', font=label_font, bg='black', fg='white')
    RB_label.grid(row=1, column=0)

    LT_label = Label(triggers_frame, text='LT: ', font=label_font, bg='black', fg='white')
    LT_label.grid(row=2, column=0)

    RT_label = Label(triggers_frame, text='RT: ', font=label_font, bg='black', fg='white')
    RT_label.grid(row=3, column=0)

    #These are the trigger Entries
    LB_entry = Entry(triggers_frame, width=10, textvariable=lb_var, font=entry_font)
    LB_entry.grid(row=0, column=1)

    RB_entry = Entry(triggers_frame, width=10, textvariable=rb_var, font=entry_font)
    RB_entry.grid(row=1, column=1)

    LT_entry = Entry(triggers_frame, width=10, textvariable=lt_var, font=entry_font)
    LT_entry.grid(row=2, column=1)

    RT_entry = Entry(triggers_frame, width=10, textvariable=rt_var, font=entry_font)
    RT_entry.grid(row=3, column=1)
    
    #Button to save all Entries and close window
    save_bindings = Button(triggers_frame, text="Save Quit", font=label_font, command=save_keys, bg='black', fg='white', 
                           activebackground='#444444', activeforeground='white')
    save_bindings.grid(row=4, column=1, columnspan=2, pady=10)

    top.mainloop()
