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

x = 1000
y = 500

toX = 1000
toY = 800

is_idle = False
is_drag = False

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
    global background_label
    global is_idle
    is_idle = True
    
    background_label.config(image=penquin_idle)
    window.after(5000, stop_idle)

def stop_idle():
    global is_idle
    is_idle = False
    background_label.config(image=penquin_walk)

def move_pet():
    global x, y, toX, toY
    global is_idle, is_drag

    if is_drag == True:
        window.after(10, move_pet)
        return
    
    if is_idle == True:
        pass
        # print("Idling...")
    elif x < toX:
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

def start_drag(event):
    global is_drag

    is_drag = True

    # window._drag_start_x = event.x
    # window._drag_start_y = event.y

    # window.geometry(f"200x200+{x}+{y}")

def do_drag(event):
    global x, y

    x = window.winfo_pointerx() -100
    y = window.winfo_pointery() -30
    window.geometry(f"+{x}+{y}")

    window.geometry(f"200x200+{x}+{y}")

def stop_drag(event):
    global is_drag

    is_drag = False
    
background_label.bind("<Button-1>", start_drag)
background_label.bind("<B1-Motion>", do_drag)
window.bind("<ButtonRelease-1>", stop_drag)


move_pet()

window.mainloop()