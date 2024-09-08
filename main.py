from tkinter import *
from tkinter import Toplevel, Label
from random import choice
import pygame

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

def restart_game():
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
        restart_button.place(x=222, y=545)
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
def light_mode():
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

def mute_unmute():
    global muted_app
    muted_app = not muted_app
    if muted_app == True:
        sound_button.configure(text="🔇")
    elif muted_app == False:
        sound_button.configure(text="🔊")
    return muted_app

def open_sets_win(root):
    
    def reset_keys():
        a_var.set('l')
        b_var.set('=')
        x_var.set('k')
        y_var.set('o')
        rb_var.set('i')
        lb_var.set('e')
        rt_var.set('p')
        lt_var.set('q')

    def save_keys():
        top.destroy()

    #Dedicate the space above to inner functions of the topLevel window under here.
    top = Toplevel(root)
    top.title("Key settings menu")
    top.geometry("400x300")
    top.resizable(False, False)
    top.configure(bg=app_bg_theme)

    global a_var, x_var, b_var, y_var
    global lb_var, rt_var, lt_var, rb_var

    entry_font = ('Roboto', 16)
    label_font = ('Roboto', 14)
    
    #These are the Button Labels
    btns_frame = Frame(top, bg=app_bg_theme)
    btns_frame.pack(side='left', anchor='n')

    A_label = Label(btns_frame, text='A: ', font=label_font, bg='lightgreen', fg='black')
    A_label.grid(row=0, column=0)

    B_label = Label(btns_frame, text='B: ', font=label_font, bg='red', fg='white')
    B_label.grid(row=1, column=0)

    X_label = Label(btns_frame, text='X: ', font=label_font, bg='blue', fg='white')
    X_label.grid(row=2, column=0)

    Y_label = Label(btns_frame, text='Y: ', font=label_font, bg='yellow')
    Y_label.grid(row=3, column=0)

    #These are the Button Entries
    A_entry = Entry(btns_frame, width=10, textvariable=a_var, font=entry_font)
    A_entry.grid(row=0, column=1)

    B_entry = Entry(btns_frame, width=10, textvariable=b_var, font=entry_font)
    B_entry.grid(row=1, column=1)

    X_entry = Entry(btns_frame, width=10, textvariable=x_var, font=entry_font)
    X_entry.grid(row=2, column=1)

    Y_entry = Entry(btns_frame, width=10, textvariable=y_var, font=entry_font)
    Y_entry.grid(row=3, column=1)

    #Button to reset all Entries
    reset_bindings = Button(btns_frame, text="Reset all", font=label_font, bg='black', fg='white', activebackground='#444444', 
                            activeforeground='white', command=reset_keys)
    reset_bindings.grid(row=4, column=0, columnspan=2, pady=10)

    #These are the trigger Labels
    triggers_frame = Frame(top, bg=app_bg_theme)
    triggers_frame.pack(side='left', anchor='n', padx=5)

    LB_label = Label(triggers_frame, text='LB: ', font=label_font, bg='black', fg='white')
    LB_label.grid(row=0, column=0)

    RB_label = Label(triggers_frame, text='RB: ', font=label_font, bg='black', fg='white')
    RB_label.grid(row=1, column=0)

    LT_label = Label(triggers_frame, text='LT: ', font=label_font, bg='black', fg='white')
    LT_label.grid(row=2, column=0)

    RT_label = Label(triggers_frame, text='RT: ', font=label_font, bg='black', fg='white')
    RT_label.grid(row=3, column=0)

    #These are the trigger Entries
    LB_entry = Entry(triggers_frame, width=10, textvariable=lb_var, font=entry_font)
    LB_entry.grid(row=0, column=1)

    RB_entry = Entry(triggers_frame, width=10, textvariable=rb_var, font=entry_font)
    RB_entry.grid(row=1, column=1)

    LT_entry = Entry(triggers_frame, width=10, textvariable=lt_var, font=entry_font)
    LT_entry.grid(row=2, column=1)

    RT_entry = Entry(triggers_frame, width=10, textvariable=rt_var, font=entry_font)
    RT_entry.grid(row=3, column=1)
    
    #Button to save all Entries and close window
    save_bindings = Button(triggers_frame, text="Save Quit", font=label_font, command=save_keys, bg='black', fg='white', 
                           activebackground='#444444', activeforeground='white')
    save_bindings.grid(row=4, column=1, columnspan=2, pady=10)

    top.mainloop()

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

#Initialize root window
root = Tk()
root.geometry("800x600")
root.title("Gamepad Helper")
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
                         font=('Roboto', 16), command=lambda: open_sets_win(root))
keys_preference.place(x=64, y=545)

sound_button = Button(root, text="🔇", font=('Roboto', 16), width=5, command=mute_unmute, fg='white', bg='black',
                      activebackground='#222222', activeforeground='white')
sound_button.place(x=118, y=545)

restart_button = Button(root, text='Restart', bg='black', fg='white', activebackground='#222222', activeforeground='white',
                         font=('Roboto', 16), command=restart_game)

# Set the background color of the first preview button
change_bgcolor()

root.bind('<Key>', hit_key)

root.mainloop()