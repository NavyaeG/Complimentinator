import os
import sys

current_dir = os.path.dirname(os.path.realpath(__file__))
sys.path.append(current_dir)

import customtkinter as ctk
from animation import Animation
from table import Table
import time
from button import Button

flag=True
animation_folder = os.path.join(current_dir, 'Animation_Folder')
compliment_db_folder = os.path.join(current_dir, 'Compliments_DB')

def button_click():
    global flag
    flag=custom_button.on_button_click()
    window.destroy()

def destroy_window():
    window.destroy()

while flag:
    # Window
    
    window = ctk.CTk()
    screen_width =  int(window.winfo_screenwidth()*0.22135)
    screen_height = int(window.winfo_screenheight()*0.25463)
    window.title("Complimentinator")
    window.geometry(f'{screen_width}x{screen_height}')

    # Table
    Table.init_db_path(compliment_db_folder)
    Table.create_table()
    compliment = Table.fetch_compliment()

    # Animation
    animation = Animation(window, animation_folder, compliment)
    animation.pack(fill="both", expand=True)
    
    #Button
    custom_button = Button(window, text="Disable", command=button_click)
    custom_button.pack(pady=10)

    # Destroy window after 2 minutes
    window.after(120000,destroy_window)

    # Run
    window.mainloop()
    if flag:
        time.sleep(17999)