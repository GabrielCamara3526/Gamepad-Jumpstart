from tkinter import *
from root_window import root
from defless_ui import timer_label, timer_state
from switches import timer_on

def end_game():
    global timer_on
    root.unbind('<Key>')

    timer_label.config(text="Time's up!")
    timer_on = False

def update_timer():
    global timer_state, timer_on

    if timer_state > 0 and timer_on == True:
        timer_state -= 1
        timer_label.configure(text=timer_state)
        root.after(1000, update_timer)
    elif timer_state == 0:
        end_game()

        