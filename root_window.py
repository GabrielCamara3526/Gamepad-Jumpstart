from tkinter import *
from game_tiles import app_bg_theme

root = Tk()
root.geometry("800x600")
root.title("Gamepad Jumpstart")
root.resizable(False, False)
root.configure(background=app_bg_theme)

#These are global in topLevel Entries and get_keyboard_to_gamepad
a_var = StringVar(value="l")
b_var = StringVar(value="=")
x_var = StringVar(value="k")
y_var = StringVar(value="o")

lb_var = StringVar(value="e")
rb_var = StringVar(value="i")
lt_var = StringVar(value="q")
rt_var = StringVar(value="p")
