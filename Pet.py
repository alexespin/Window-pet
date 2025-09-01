import sys
import os
import tkinter as tk
from PIL import Image, ImageTk

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        base_path = sys._MEIPASS
    except AttributeError:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

window = tk.Tk()
window.geometry("200x200")
window.title("Pet")

img = Image.open(resource_path("penguin.png"))
img = img.resize((200, 200), Image.LANCZOS)

img2 = Image.open(resource_path("penguin_sitting.png"))
img2 = img2.resize((200, 200), Image.LANCZOS)

penquin_walk = ImageTk.PhotoImage(img)
penquin_idle = ImageTk.PhotoImage(img2)

background_label = tk.Label(window, image=penquin_walk)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

x = 1640
y = 500

toX = 1000
toY = 800

screen_width = window.winfo_screenwidth()-280
screen_height = window.winfo_screenheight()-280
print(f"Screen width: {screen_width}, Screen height: {screen_height}")

def random_move():
    import random

    global toX, toY
    
    pick = random.randint(0, 1)
    print(f"Random pick: {pick}")
    if pick == 0:
        toX = random.randint(0, screen_width)
        toY = random.randint(0, screen_height)
    else:
        idle()

    print(f"New target position: ({toX}, {toY})")

def idle():
    import time
    global background_label

    print("Idling...")
    background_label.config(image=penquin_idle)
    window.update()
    time.sleep(5)
    background_label.config(image=penquin_walk)

def move_pet():
    global x, y, toX, toY

    if x < toX:
        x += 1
    elif x > toX:
        x -= 1
    elif y < toY:
        y += 1
    elif y > toY:
        y -= 1
    else:
        random_move()

    window.geometry(f"200x200+{x}+{y}") 
    # print(f"Current position: ({x}, {y})")
    
    window.after(10, move_pet)


move_pet()

window.mainloop()