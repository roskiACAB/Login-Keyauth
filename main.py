from keyauth import api
import sys
import time
import platform
import os
import hashlib
from time import sleep
from datetime import datetime
import tkinter
import customtkinter
import ctypes


def remove_logo(window):
    hwnd = ctypes.windll.user32.GetParent(window.winfo_id())
    style = ctypes.windll.user32.GetWindowLongW(hwnd, -16)
    style &= ~0x00080000
    ctypes.windll.user32.SetWindowLongW(hwnd, -16, style)
    ctypes.windll.user32.ShowWindow(hwnd, 0x0)

def screenopen(screen, width, height):
    screen_width = screen.winfo_screenwidth()
    screen_height = screen.winfo_screenheight()

    x = (screen_width - width) // 2
    y = (screen_height - height) // 2

    screen.geometry(f"{width}x{height}+{x}+{y}")

def clear():
    if platform.system() == 'Windows':
        os.system('cls & title Python Example')

def getchecksum():
    md5_hash = hashlib.md5()
    file = open(''.join(sys.argv), "rb")
    md5_hash.update(file.read())
    digest = md5_hash.hexdigest()
    return digest


keyauthapp = api(
    name = "",
    ownerid = "",
    secret = "",
    version = "",
    hash_to_check = getchecksum()
)

def answer():
    # Login window settings
    login = customtkinter.CTk()
    screenopen(login, 400, 300)
    login.title("Name App")
    login.wm_attributes('-transparentcolor', '#ab23ff')
    login.config(bg="#ab23ff")
    #Delete - [] x and icon in title
    remove_logo(login)

    # Text (Your app name)
    label = customtkinter.CTkLabel(login, text="App Name", fg_color="#343434", text_color="white", font=customtkinter.CTkFont(size=24, weight="bold", family="Montserrat"), width=70,height=50, corner_radius=6,)
    label.place(x=150, y=50)
    # Space to fill
    loginentry = customtkinter.CTkEntry(master=login, width=220, placeholder_text=' License')
    loginentry.place(x=100, y=150)


    #Checkking license and next steps
    def loginstep():
        key = loginentry.get()
        keyauthapp.license(key)

        #Close login window
        login.destroy()

        #In this line, you can add a function, etc. If the license is correct, the function is run
        print("your further code!")


    def closelogin():
        login.destroy()

    # Button to confirm license
    button = customtkinter.CTkButton(master=login, text="Login", command=loginstep, fg_color="#343434", hover_color="#212121")
    button.place(x=145, y=200)

    button = customtkinter.CTkButton(master=login,
                                     text="×",
                                     command=closelogin,
                                     width=30,
                                     height=30,
                                     fg_color="#343434",
                                     hover_color="#212121")
    button.place(x=365, y=265)


    login.mainloop()


answer()

os._exit(1)
