from tkinter import *
import pygame
pygame.init()

#App info like Sounds, buttons and their colors, etc...
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
