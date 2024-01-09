import keyboard;
from tkinter import *
import sys
from pygame import mixer
from pygame.mixer import Sound
import pystray
from pystray import MenuItem as item
from PIL import Image


base_path = getattr(sys, '_MEIPASS','.')+'/'

startButton = True;

mixer.pre_init(22050, -16, 1, 256)
mixer.init()

charDown = Sound(base_path + "sounds\D.wav")

charUp = Sound(base_path + r"sounds\U.wav")

backspaceDown = Sound(base_path + "sounds\BSPD.wav")

backspaceUp = Sound(base_path + "sounds\BSPU.wav")

enterDown = Sound(base_path + "sounds\ED.wav")

enterUp = Sound(base_path + "sounds\EU.wav")
            
spaceDown = Sound(base_path + "sounds\SD.wav")

spaceUp = Sound(base_path + "sounds\SU.wav")

smallSizeKeyDown = Sound(base_path + "sounds\smallSizeKeyD.wav")

smallSizeKeyUp = Sound(base_path + "sounds\smallSizeKeyU.wav")

shiftDown = Sound(base_path + "sounds\ShD.wav")

shiftUp = Sound(base_path + "sounds\ShU.wav")

midDown = Sound(base_path + "sounds\midD.wav")

midUp = Sound(base_path + "sounds\midU.wav")

def charDownSound(event):
    Sound.play(charDown)
def charUpSound(event):
    Sound.play(charUp)

def enterDownSound(event):
    Sound.play(enterDown)
def enterUpSound(event):
    Sound.play(enterUp)

def backspaceDownSound(event):
    Sound.play(backspaceDown)
def backspaceUpSound(event):
    Sound.play(backspaceUp)

def spaceDownSound(event):
    Sound.play(spaceDown)
def spaceUpSound(event):
    Sound.play(spaceUp)

def smallSizeKeyDownSound(event):
    Sound.play(smallSizeKeyDown)
def smallSizeKeyUpSound(event):
    Sound.play(smallSizeKeyUp)

def shiftDownSound(event):
    Sound.play(shiftDown)
def shiftUpSound(event):
    Sound.play(shiftUp)

def midDownSound(event):
    Sound.play(midDown)
def midUpSound(event):
    Sound.play(midUp)

def start() :

    characters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'f1', 'f2', 'f3', 'f4', 'f5', 'f6', 'f7', 'f8', 'f9', 'f10', 'f11', 'f12', 'Page up', 'Page down', 'home', 'delete', 'end', 'insert', 'scroll lock', 'num lock', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '-', '=', '~', 'esc', 'left', 'right', 'up', 'down', 'print screen', 'pause', '/', '\'', ']', '[', ';', ',', '.']

    for key in characters :
        keyboard.on_press_key(key, charDownSound, suppress=False)
        keyboard.on_release_key(key, charUpSound, suppress=False)

    keyboard.on_press_key('enter', enterDownSound, suppress=False)
    keyboard.on_release_key('enter', enterUpSound, suppress=False)

    keyboard.on_press_key('backspace', backspaceDownSound, suppress=False)
    keyboard.on_release_key('backspace', backspaceUpSound, suppress=False)

    keyboard.on_press_key('space', spaceDownSound, suppress=False)
    keyboard.on_release_key('space', spaceUpSound, suppress=False)

    smallSizeKeys = ['ctrl', 'alt', 'alt gr', 'windows', 'menu']

    for key in smallSizeKeys :
        keyboard.on_press_key(key, smallSizeKeyDownSound, suppress=False)
        keyboard.on_release_key(key, smallSizeKeyUpSound, suppress=False)

    keyboard.on_press_key('shift', shiftDownSound, suppress=False)
    keyboard.on_release_key('shift', shiftUpSound, suppress=False)

    midSizeKeys = ['tab', 'caps lock', '\\']

    for key in midSizeKeys :
        keyboard.on_press_key(key, midDownSound, suppress=False)
        keyboard.on_release_key(key, midUpSound, suppress=False)

# GUI link

def btn_clicked():
    global startButton
    if startButton:
        startButton = False
        b0.configure(image=img1)
        canvas.itemconfig(background, state='hidden') 
        canvas.itemconfig(background1, state='normal')
        start()
    else :
        window.destroy()



# GUI



window = Tk()

window.wm_title("Mechanical Keyboard Simulator")
window.iconbitmap(base_path + "MKS logo small.ico")

window.geometry("703x500")
window.configure(bg = "#ffffff")
canvas = Canvas(
    window,
    bg = "#ffffff",
    height = 500,
    width = 703,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge")
canvas.place(x = 0, y = 0)

img0 = PhotoImage(file = base_path + "img0.png")
img1 = PhotoImage(file = base_path + "img1.png")

b0 = Button(
    image = img0,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

b0.place(
    x = 224, y = 352,
    width = 256,
    height = 64)

background_img = PhotoImage(file = base_path + "background.png")
background = canvas.create_image(
    352.0, 202.5,
    image=background_img)

background_img1 = PhotoImage(file = base_path + "background1.png")
background1 = canvas.create_image(
    351.5, 250.0,
    image=background_img1)
canvas.itemconfig(background1, state='hidden')


# Show in system tray

def quit_window(icon, item):
    icon.stop()
    window.destroy()

def show_window(icon, item):
    icon.stop()
    window.after(0,window.deiconify)
    

def withdraw_window():  
    window.withdraw()
    image = Image.open(base_path + "MKS logo small.ico")
    menu = (item('Quit', quit_window), item('Show', show_window))
    global icon;
    icon = pystray.Icon("MKS", image, "MKS", menu)
    icon.run()

def closeOrWithdraw() :
    if startButton :
        window.destroy()
    else :
        withdraw_window()

window.protocol('WM_DELETE_WINDOW', closeOrWithdraw)

window.resizable(False, False)
window.mainloop()
