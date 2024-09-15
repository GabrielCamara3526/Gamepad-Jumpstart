from tkinter import *
from root_window import root
from random import choice
from game_tiles import gamepad_buttons

#All main screen widgets not related to functions
top_frame = Frame(root, bg='#30d30d30d', relief=SUNKEN, borderwidth=1)
top_frame.pack(side=TOP, anchor='center', fill=X, pady=5)

timer_reference = Label(root, text='Timer', font=('Helvetica', 12), bg='#30d30d30d', fg='white')
timer_reference.place(x=0, y=80)

score_reference = Label(root, text='Score', font=('Helvetica', 12), bg='#30d30d30d', fg='white')
score_reference.place(x=741, y=80)

timer_state = 60
timer_label = Label(top_frame, text=timer_state, font=('Roboto', 28), bg='#30d30d30d', fg='white', bd=1, 
                    highlightthickness=0)
timer_label.pack(anchor='w', side='left')

points_label = Label(top_frame, text='0', font=('Roboto', 28), bg='#30d30d30d', fg='white', bd=0, highlightthickness=0)
points_label.pack(anchor='e', side='right')


preview_nxt_btn = Button(root, text=choice(gamepad_buttons), 
                         font=('Helvetica',16), width=7, height=3,fg='white' )
preview_nxt_btn.place(x=625, y=250)

