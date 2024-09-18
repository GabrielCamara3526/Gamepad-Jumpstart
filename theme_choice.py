from tkinter import *
from defless_ui import points_label, top_frame, timer_reference, score_reference
from root_window import root
from switches import lights_off

#Handles the click on theme_changer button. if lights_off is true, sets widgets to brighter color.
def light_mode(event=NONE):
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

#User options buttons. These stay in the bottom left corner of the root win.
theme_changer = Button(root, text="🔆", command=light_mode, font=('Roboto', 16), bg='black',
                       activebackground='#222222')
theme_changer.place(x=0, y=545)
