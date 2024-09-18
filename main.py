from tkinter import *
from tkinter import Toplevel, Label
from random import choice
import pygame # type: ignore
from game_tiles import gamepad_colors, app_bg_theme, gamepad_buttons, correct_sound, wrong_sound, soundless_keys, points_counter
from root_window import root
from root_window import a_var, b_var, x_var, y_var
from root_window import lb_var, rb_var, lt_var, rt_var
from key_settings import open_sets_win
from defless_ui import timer_state, timer_reference, score_reference, points_label, preview_nxt_btn, timer_label, top_frame
from switches import timer_on, muted_app, lights_off
from theme_choice import light_mode


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
    points_label.configure(text=points_counter)


def change_bgcolor():
    current_text = game_button.cget("text")
    current_preview_txt = preview_nxt_btn.cget("text")

    game_button.configure(bg=gamepad_colors[current_text])
    preview_nxt_btn.configure(bg=gamepad_colors[current_preview_txt])
    if current_text in ["LB", "RB", "LT", "RT"]:
        game_button.configure(fg='white')
    else:
        game_button.configure(fg='black')

    if current_preview_txt in ["LB", "RB", "LT", "RT"]:
        preview_nxt_btn.configure(fg='white')
    elif current_preview_txt in ["A", "B", "X", "Y"]:
        preview_nxt_btn.configure(fg='black')

#Called on hit_key. Get preview_ntx_btn text and bring it to game_button then set a new random text to preview button.
def new_game_button():
    game_button.configure(text=preview_nxt_btn.cget("text"))
    preview_nxt_btn.configure(text=choice(gamepad_buttons))
    change_bgcolor()

#Get the key that is pressed and compare it to the current random text coming from game_button.
def hit_key(event):
    current_text = game_button.cget("text")
    #key receives the pressed character on the keyboard. Keysym is the same except it doesn't take modifiers.
    key = event.char
    keysym = event.keysym

    if key in get_keyboard_to_gamepad() and get_keyboard_to_gamepad()[key] == current_text:
        if not muted_app:
            correct_sound.play()

        start_timer()
        slide_right()
        count_point()

        root.after(100, new_game_button)

    elif keysym not in soundless_keys:
        if not muted_app:
            wrong_sound.play()

def restart_game(event):
    global timer_state, points_counter, timer_on
    root.bind('<Key>', hit_key)
    restart_button.place_forget()
    timer_on = False
    timer_state = 60

    points_counter = 0
    timer_label.config(text=timer_state)
    points_label.config(text=points_counter)

def slide_left():
    global my_x
    if my_x > 390:
        my_x -= 8
        game_button.place(x=my_x)
        root.after(10, slide_left)

def slide_right():
    global my_x
    if my_x < 450:
        my_x += 8
        game_button.place(x=my_x)
        root.after(5, slide_right)
    else:
        root.after(100, slide_left)

def mute_unmute(event=NONE):
    global muted_app
    muted_app = not muted_app
    if muted_app == True:
        sound_button.configure(text="🔇")
    elif muted_app == False:
        sound_button.configure(text="🔊")
    return muted_app

def start_timer():
    global timer_on

    if timer_on == False:
        timer_on = True
        restart_button.place(x=223, y=545)
        update_timer()
    
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

pygame.init()

initial_button = choice(gamepad_buttons)

if initial_button in ["Y"]:
    initial_fgcolor = "black"
else:
    initial_fgcolor = "white"

global my_x
my_x = 390
game_button = Button(root, text=initial_button, font=('Helvetica',32), 
                     bg=gamepad_colors[initial_button], 
                     fg=initial_fgcolor, height=5, width=10, command=new_game_button, 
                     bd=0, highlightthickness=0)
game_button.place(x=my_x, y=600/2, anchor='center')

keys_preference = Button(root, text="⚙️", bg='black', fg='white', activebackground='#222222', activeforeground='white',
                         font=('Roboto', 16), command=lambda: open_sets_win(root, event=NONE))
keys_preference.place(x=64, y=545)

sound_button = Button(root, text="🔇", font=('Roboto', 16), width=5, command=mute_unmute, fg='white', bg='black',
                      activebackground='#222222', activeforeground='white')
sound_button.place(x=118, y=545)


restart_button = Button(root, text='Restart', bg='black', fg='white', activebackground='#222222', activeforeground='white',
                         font=('Roboto', 16), command=lambda: restart_game(event=NONE))

# Set the background color of the first preview button
change_bgcolor()

root.bind('<Key>', hit_key)
root.bind('<Control-Shift-R>', restart_game)
root.bind('<Control-Shift-M>', mute_unmute)
root.bind('<Control-Shift-S>', lambda event: open_sets_win(root, event))
root.bind('<Control-Shift-T>', light_mode)

root.mainloop()