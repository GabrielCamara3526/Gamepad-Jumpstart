from tkinter import *
from tkinter import Toplevel, Label
from random import choice
import pygame

def get_keyboard_to_gamepad():
    return {
        'l': 'A', '=': 'B', 'k': 'X', 'o': 'Y',
        'e': 'LB','i': 'RB', 'q': 'LT', 'p': 'RT'
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
        slide_right()
        count_point()
        root.after(100, new_game_button)
    elif keysym not in soundless_keys:
        if not muted_app:
            wrong_sound.play()
           
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

#Handles the click on theme_changer button. if lights_off is true, sets widgets to brighter color.
def light_mode():
    global lights_off
    if lights_off:
        root.configure(bg="#d9d9d9")
        points_label.configure(bg="#d9d9d9")
        points_label.configure(fg="black")
        theme_changer.configure(text='🌙')
        lights_off = False
    else:
        root.configure(bg="#30d30d30d")
        points_label.configure(bg="#30d30d30d")
        points_label.configure(fg="white")
        theme_changer.configure(text="🔆")
        lights_off = True

def mute_unmute():
    global muted_app
    muted_app = not muted_app
    if muted_app == True:
        sound_button.configure(text="🔇")
    elif muted_app == False:
        sound_button.configure(text="🔊")
    return muted_app

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

pygame.init()

correct_sound = pygame.mixer.Sound("correctanswer.mp3")
wrong_sound = pygame.mixer.Sound("wronganswer.mp3")


gamepad_buttons = ["A", "B", "X", "Y", "LB", "RB", "LT", "RT"]


gamepad_colors = {"A": "#0ec809", "B": "red", "X": "blue", "Y": "yellow",
                  "LB": "#181818", "RB": "#181818", "LT": "#181818", "RT": "#181818"}

points_counter = 0
app_bg_theme = '#30d30d30d'
soundless_keys = ["Alt_L", "BackSpace", "Shift_L", "Shift_R", "KP_Enter", "Return", "Tab", 
                  "Caps_Lock", "Control_L", "Control_R", "KP_Divide", "Num_Lock", "apostrophe", 
                  "Left", "Right", "Down", "Up", 'Escape', "F1", "F2", "F3", "F4", "F5", "F6", 
                  "F7", "F8", "F9", "F10", "F11", "F12", 'Delete', 'End', 'Insert', 'Home','Prior', 'Next', 'space']

root = Tk()
root.geometry("800x600")
root.title("Gamepad Helper")
root.resizable(False, False)
root.configure(background=app_bg_theme)

top_frame = Frame(root)
top_frame.pack(side='top', anchor='e')

points_label = Label(root, text='0', font=('Roboto', 28), bg='#30d30d30d', fg='white', bd=0, highlightthickness=0)
points_label.pack(anchor='center', side='top')

game_frame = Frame(root, bg='#30d30d30d')
game_frame.pack(side='bottom', pady=(0, 145))

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

theme_changer = Button(root, text="🔆", command=light_mode, font=('Roboto', 16), bg='black',
                       activebackground='#222222')
theme_changer.place(x=0, y=545)

keys_preference = Button(root, text="⚙️", bg='black', fg='white', activebackground='#222222', activeforeground='white',
                         font=('Roboto', 16), command=lambda: open_sets_win(root))
keys_preference.place(x=64, y=545)

sound_button = Button(root, text="🔇", font=('Roboto', 16), width=5, command=mute_unmute, fg='white', bg='black',
                      activebackground='#222222', activeforeground='white')
sound_button.place(x=118, y=545)

# Set the background color of the first preview button
change_bgcolor()

root.bind('<Key>', hit_key)

root.mainloop()