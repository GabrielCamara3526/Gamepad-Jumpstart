from tkinter import *
from tkinter import Toplevel, Label
from random import choice
import pygame
from game_tiles import gamepad_colors, app_bg_theme, gamepad_buttons, correct_sound, wrong_sound, soundless_keys, points_counter
from root_window import root
from keys_settings import open_sets_win
from root_window import *

def get_keyboard_to_gamepad():
    global a_var, b_var, x_var, y_var
    global lb_var, rb_var, lt_var, rt_var
    return {
        a_var.get(): 'A', b_var.get(): 'B', x_var.get(): 'X', y_var.get(): 'Y',
        lb_var.get(): 'LB', rb_var.get(): 'RB', lt_var.get(): 'LT', rt_var.get(): 'RT'
    }

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

def count_point():
    global points_counter
    points_counter += 1
    points_label.configure(text=str(points_counter))

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


def end_game():
    global timer_on
    root.unbind('<Key>')

    timer_label.config(text="Time's up!")
    timer_on = False

def restart_game(event):
    global timer_state, points_counter, timer_on
    root.bind('<Key>', hit_key)
    restart_button.place_forget()
    timer_on = False
    timer_state = 60

    points_counter = 0
    timer_label.config(text=timer_state)
    points_label.config(text=points_counter)

def update_timer():
    global timer_state, timer_on

    if timer_state > 0 and timer_on == True:
        timer_state -= 1
        timer_label.configure(text=timer_state)
        root.after(1000, update_timer)
    elif timer_state == 0:
        end_game()


def start_timer():
    global timer_on

    if timer_on == False:
        timer_on = True
        restart_button.place(x=223, y=545)
        update_timer()
    

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

#These work like On/Off Switches: App Starts in Dark mode (lights_off) and Muted. 
lights_off = True 
muted_app = True
timer_on = False

#Handles the click on theme_changer button. if lights_off is true, sets widgets to brighter color.
def light_mode(event):
    global lights_off
    if lights_off:
        root.configure(bg="#d9d9d9")
        points_label.configure(bg="#d9d9d9")
        points_label.configure(fg="black")
        top_frame.configure(bg='#d9d9d9')

        timer_reference.configure(bg='#d9d9d9')
        timer_reference.configure(fg='black')

        score_reference.configure(bg='#d9d9d9')
        score_reference.configure(fg='black')

        theme_changer.configure(text='🌙')
        lights_off = False
    else:
        root.configure(bg="#30d30d30d")
        top_frame.configure(bg='#30d30d30d')
        points_label.configure(bg="#30d30d30d")
        points_label.configure(fg="white")

        timer_reference.configure(bg='#30d30d30d')
        timer_reference.configure(fg='white')

        score_reference.configure(bg='#30d30d30d')
        score_reference.configure(fg='white')

        theme_changer.configure(text="🔆")
        lights_off = True

def mute_unmute(event=NONE):
    global muted_app
    muted_app = not muted_app
    if muted_app == True:
        sound_button.configure(text="🔇")
    elif muted_app == False:
        sound_button.configure(text="🔊")
    return muted_app

pygame.init()

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


preview_nxt_btn = Button(root, text=choice(gamepad_buttons), 
                         font=('Helvetica',16), width=7, height=3,fg='white' )
preview_nxt_btn.place(x=625, y=250)

#User options buttons. These stay in the bottom left corner of the root win.
theme_changer = Button(root, text="🔆", command=light_mode, font=('Roboto', 16), bg='black',
                       activebackground='#222222')
theme_changer.place(x=0, y=545)

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