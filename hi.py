from tkinter import *
from tkinter import Toplevel, Label
from random import choice
import pygame

pygame.init()

correct_sound = pygame.mixer.Sound("correctanswer.mp3")
wrong_sound = pygame.mixer.Sound("wronganswer.mp3")


gamepad_buttons = ["A", "B", "X", "Y", "LB", "RB", "LT", "RT"]


gamepad_colors = {"A": "#0ec809", "B": "red", "X": "blue", "Y": "yellow",
                  "LB": "#181818", "RB": "#181818", "LT": "#181818", "RT": "#181818"}


points_counter = 0
muted_effects = False

root = Tk()
root.geometry("800x600")
root.title("Gamepad Helper")
root.configure(bg='#30d30d30d')

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
    else:
        preview_nxt_btn.configure(fg='black')

def count_point():
    global points_counter
    points_counter += 1
    points_label.configure(text=str(points_counter))

def new_game_button():
    game_button.configure(text=preview_nxt_btn.cget("text"))
    preview_nxt_btn.configure(text=choice(gamepad_buttons))
    change_bgcolor()

def hit_key(event):
    current_text = game_button.cget("text")
    key = event.char

    if key in get_keyboard_to_gamepad() and get_keyboard_to_gamepad()[key] == current_text:
        count_point()
        new_game_button()

def slide_animation():
    pass

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

game_button = Button(game_frame, text=initial_button, font=('Helvetica',32), 
                     bg=gamepad_colors[initial_button], 
                     fg=initial_fgcolor, height=5, width=10, command=new_game_button, 
                     bd=0, highlightthickness=0)
game_button.grid(row=0,column=0, padx=(10, 0), pady=(0, 20))


preview_nxt_btn = Button(root, text=choice(gamepad_buttons), 
                         font=('Helvetica',16), width=7, height=3,fg='white' )
preview_nxt_btn.place(x=625, y=250)

# Set the background color of the first preview button
initial_bgpreview = preview_nxt_btn.cget("text")
preview_nxt_btn.configure(bg=gamepad_colors[initial_bgpreview])

root.bind('<Key>', hit_key)

root.mainloop()
