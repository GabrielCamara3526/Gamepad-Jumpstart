from tkinter import *
from root_window import *
from defless_ui import points_label
from game_tiles import points_counter

#Used in hit_key to check if pressed key equals current button text
def get_keyboard_to_gamepad():
    global a_var, b_var, x_var, y_var
    global lb_var, rb_var, lt_var, rt_var
    return {
        a_var.get(): 'A', b_var.get(): 'B', x_var.get(): 'X', y_var.get(): 'Y',
        lb_var.get(): 'LB', rb_var.get(): 'RB', lt_var.get(): 'LT', rt_var.get(): 'RT'
    }

def count_point():
    global points_counter
    points_counter += 1
    points_label.configure(text=str(points_counter))
