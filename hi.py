from tkinter import *
from tkinter import Toplevel, Label
from random import choice
import pygame

# Initialize the pygame mixer
pygame.init()

# Load sound effects
correct_sound = pygame.mixer.Sound("correctanswer.mp3")
wrong_sound = pygame.mixer.Sound("wronganswer.mp3")

# Define gamepad buttons
gamepad_buttons = ["A", "B", "X", "Y", "LB", "RB", "LT", "RT"]

# Define colors for each gamepad button
gamepad_colors = {"A": "#0ec809", "B": "red", "X": "blue", "Y": "yellow",
                  "LB": "#181818", "RB": "#181818", "LT": "#181818", "RT": "#181818"}

# Initialize points counter and mute state
points_counter = 0
muted_effects = False

# Create the main Tkinter window
root = Tk()
root.geometry("800x600")
root.title("Gamepad Helper")

# Define StringVars for all entries
A_var = StringVar(value="l")
B_var = StringVar(value="=")
X_var = StringVar(value="k")
Y_var = StringVar(value="o")
LB_var = StringVar(value="e")
RB_var = StringVar(value="i")
LT_var = StringVar(value="q")
RT_var = StringVar(value="p")

# Define mapping of keyboard keys to gamepad buttons
def get_keyboard_to_gamepad():
    return {
        A_var.get(): 'A', B_var.get(): 'B', X_var.get(): 'X', Y_var.get(): 'Y',
        LB_var.get(): 'LB', RB_var.get(): 'RB', LT_var.get(): 'LT', RT_var.get(): 'RT'
    }

# Function to change the background color of the game button based on its text
def change_bgcolor():
    current_text = game_button.cget("text")
    game_button.configure(bg=gamepad_colors[current_text])
    if current_text in ["LB", "RB", "LT", "RT"]:
        game_button.configure(fg='white')  # Set text color to white for dark buttons
    else:
        game_button.configure(fg='black')  # Set text color to black for light buttons

# Function to increase the points counter
def count_point():
    global points_counter
    points_counter += 1
    points_label.configure(text=str(points_counter))

def reduce_point():
    global points_counter
    points_counter -= 1
    points_label.configure(text=str(points_counter))

# Function to select a new game button randomly
def new_game_button():
    game_button.configure(text=choice(gamepad_buttons))
    change_bgcolor()

# Function to handle key presses
def hit_key(event):
    global muted_effects
    current_text = game_button.cget("text")
    key = event.char

    if key in get_keyboard_to_gamepad() and get_keyboard_to_gamepad()[key] == current_text:
        count_point()
        new_game_button()
        if not muted_effects:
            correct_sound.play()
    else:
        if points_counter > 0:
            reduce_point()
            if not muted_effects:
                wrong_sound.play()

# Function to toggle mute state
def mute_unmute(event=None):
    global muted_effects
    muted_effects = not muted_effects
    mute_button.configure(text='Unmute 🔇' if muted_effects else 'Mute 🔊')

def default_keys():
    global A_var, B_var, X_var, Y_var, LB_var, RB_var, LT_var, RT_var 
    A_var.set("l")
    B_var.set("=")
    X_var.set("k")
    Y_var.set("o")
    LB_var.set("e")
    RB_var.set("i")
    LT_var.set("q")
    RT_var.set("p")

def keys_menu():
    keys_window = Toplevel(root)
    keys_window.title("Keys preference")
    keys_window.geometry("500x300")

    main_frame = Frame(keys_window)
    main_frame.grid(row=0, column=2, sticky='n')

    def validate_input(new_value):
         return len(new_value) <= 1

    vcmd = keys_window.register(validate_input)

    # Define button labels
    A_label = Label(main_frame, text='A:', font=('Arial', 14))
    A_label.grid(row=0, column=0, padx=10, pady=5, sticky='w')
    
    B_label = Label(main_frame, text='B:', font=('Arial', 14))
    B_label.grid(row=1, column=0, padx=10, pady=5, sticky='w')
    
    X_label = Label(main_frame, text='X:', font=('Arial', 14))
    X_label.grid(row=2, column=0, padx=10, pady=5, sticky='w')
    
    Y_label = Label(main_frame, text='Y:', font=('Arial', 14))
    Y_label.grid(row=3, column=0, padx=10, pady=5, sticky='w')

    # Define button entry widgets and associate them with StringVar
    A_entry = Entry(main_frame, width=8,validate="key", validatecommand=(vcmd, '%P'), textvariable=A_var, font=('Helvetica', 18))
    A_entry.grid(row=0, column=1, padx=10, pady=5)

    B_entry = Entry(main_frame, width=8, validatecommand=(vcmd, '%P'), textvariable=B_var, font=('Helvetica', 18))
    B_entry.grid(row=1, column=1, padx=10, pady=5)

    X_entry = Entry(main_frame, width=8, validatecommand=(vcmd, '%P'), textvariable=X_var, font=('Helvetica', 18))
    X_entry.grid(row=2, column=1, padx=10, pady=5)

    Y_entry = Entry(main_frame, width=8, validatecommand=(vcmd, '%P'), textvariable=Y_var, font=('Helvetica', 18))
    Y_entry.grid(row=3, column=1, padx=10, pady=5)

    # Define trigger labels
    LB_label = Label(main_frame, text='LB:', font=('Arial', 14))
    LB_label.grid(row=0, column=2, padx=10, pady=5, sticky='w')
    
    RB_label = Label(main_frame, text='RB:', font=('Arial', 14))
    RB_label.grid(row=1, column=2, padx=10, pady=5, sticky='w')
    
    LT_label = Label(main_frame, text='LT:', font=('Arial', 14))
    LT_label.grid(row=2, column=2, padx=10, pady=5, sticky='w')
    
    RT_label = Label(main_frame, text='RT:', font=('Arial', 14))
    RT_label.grid(row=3, column=2, padx=10, pady=5, sticky='w')

    # Define Trigger entry widgets and associate them with StringVar
    LB_entry = Entry(main_frame, width=8, validatecommand=(vcmd, '%P'), textvariable=LB_var, font=('Helvetica', 18))
    LB_entry.grid(row=0, column=3, padx=10, pady=5)

    RB_entry = Entry(main_frame, width=8, validatecommand=(vcmd, '%P'), textvariable=RB_var, font=('Helvetica', 18))
    RB_entry.grid(row=1, column=3, padx=10, pady=5)

    LT_entry = Entry(main_frame, width=8, validatecommand=(vcmd, '%P'), textvariable=LT_var, font=('Helvetica', 18))
    LT_entry.grid(row=2, column=3, padx=10, pady=5)

    RT_entry = Entry(main_frame, width=8, validatecommand=(vcmd, '%P'), textvariable=RT_var, font=('Helvetica', 18))
    RT_entry.grid(row=3, column=3, padx=10, pady=5)

    bottom_frame = Frame(keys_window)
    bottom_frame.grid(row=4, column=2, pady=45, padx=45)

    set_default = Button(bottom_frame, text='Set Default', font=('Helvetica', 14), command=default_keys)
    set_default.grid()

# Create the top frame to hold the set keys button
top_frame = Frame(root)
top_frame.pack(side='top', anchor='e')

# Create the set keys button and place it in the top frame
set_keys = Button(top_frame, text='Set Keys', font=('Roboto', 18), command=keys_menu)
set_keys.pack(side='right')

# Create the points label and place it in the main window
points_label = Label(root, text='0', font=('Roboto', 28))
points_label.pack(anchor='center', side='top')

# Create the mute button and place it in the main window
mute_button = Button(root, text='Mute 🔊', font=('Roboto', 28),
                     width=13, height=2,bg='#34b4eb', command=mute_unmute)
mute_button.pack(side='bottom')

# Create the game button with an initial random gamepad button and place it in the main window
initial_button = choice(gamepad_buttons)
initial_fgcolor = "white"
game_button = Button(root, text=initial_button, font=('Helvetica', 24), bg=gamepad_colors[initial_button], fg=initial_fgcolor, height=7, width=16, command=new_game_button)
game_button.pack(side='bottom', pady=10)

# Call function to set initial background color
change_bgcolor()

# Bind key press events to the hit_key function
root.bind('<Key>', hit_key)
root.bind('<m>', mute_unmute)  # Corrected binding for the 'm' key

# Start the main event loop
root.mainloop()