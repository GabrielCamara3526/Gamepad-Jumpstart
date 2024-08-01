from tkinter import *
from random import choice
import pygame

pygame.init()

correct_sound = pygame.mixer.Sound("correctanswer.mp3")
wrong_sound = pygame.mixer.Sound("wronganswer.mp3")

gamepad_buttons = ["A", "B", "X", "Y", "LB", "RB", "LT", "RT"]

keyboard_to_gamepad = {"l": 'A', "=": 'B', "k": 'X', "o": 'Y', "e": 'LB', "i":'RB', "q": 'LT', "p": 'RT'}

gamepad_colors = {"A": "#0ec809", "B": "red", "X": "blue", "Y": "yellow", 
                  "LB": "#181818", "RB": "#181818", "LT": "#181818", "RT":"#181818"}
points_counter = 0

def change_bgcolor():
    current_text = game_button.cget("text")
    game_button.configure(bg=gamepad_colors[current_text])
    if current_text in "LB" or current_text in "RB" or current_text in "LT" or current_text in "RT":
        game_button.configure(fg='white')

def count_point():
    global points_counter
    points_counter += 1
    points_label.configure(text=str(points_counter))

def new_game_button():
    game_button.configure(text=choice(gamepad_buttons))
    change_bgcolor()

def hit_key(event):
    current_text = game_button.cget("text")
    key = event.char
    if key in keyboard_to_gamepad and keyboard_to_gamepad[key] == current_text:
        count_point()
        new_game_button()
        correct_sound.play()
    else:
        wrong_sound.play()

root = Tk()
root.geometry("800x600")
root.title("Gamepad Helper")

points_label = Label(root, text='0', font=('Roboto', 24))
points_label.pack()

initial_button = choice(gamepad_buttons)
initial_fgcolor = "white"
game_button = Button(root, text=initial_button, font=('Helvetica', 24), bg=gamepad_colors[initial_button], fg=initial_fgcolor, height=5, width=30, command=new_game_button)
game_button.pack(side='bottom', pady=75)

root.bind('<Key>', hit_key)
root.mainloop()
