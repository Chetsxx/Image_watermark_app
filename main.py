from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from tkinter import colorchooser
from PIL import ImageTk, Image
from fontbox import FontBox



color = "white"

def UploadAction(event=None):
    filename = filedialog.askopenfilename(title='open', filetype=(("jpeg", "*.jpg"), ("png", "*.png")))
    image_path = Image.open(filename)
    image_path = image_path.resize((700, 500), Image.ANTIALIAS)
    canvas.create_image(0, 0, image=photo, anchor='nw')
    canvas.image = photo

def font_chooser(event=None):
    FontBox()

def start_drawing():
    global color
    color = colorchooser.askcolor()[1]

def getx_gety(event):
    global lasx, lasy
    lasx, lasy = event.x, event.y

def draw(event):
    global lasx, lasy
    global color
    canvas.create_line((lasx, lasy, event.x, event.y), fill=color, width=1)
    lasx, lasy = event.x, event.y



window = Tk()
window.title('Watermarker')
window.geometry("700x500")
window.resizable(True, True)
window.config(padx=10, pady=10)
window.grid_rowconfigure(0, weight=1)
window.grid_columnconfigure(0, weight=1)

size = ttk.Sizegrip(window)
size.grid(row=1, sticky=SW)

title = Label(text="Image Watermarker", font=("Ariel", 24, "bold"), fg="blue")
title.grid(row=0, column=0, columnspan=3)

canvas = Canvas(window, bg="white", width=700, height=500)
canvas.grid(row=1, column=0, columnspan=1, rowspan=6, sticky=NW, padx=10, pady=10)
canvas.bind("<Button-1>", getx_gety)
canvas.bind("<B1-Motion>", draw)


open_img = Button(window, text='Open Image', command=UploadAction)
open_img.grid(row=1, column=2)

font_style = Button(window, text='Pick a Font', command=font_chooser)
font_style.grid(row=3, column=2)

draw = Button(window, text='Pick a color', command=start_drawing)
draw.grid(row=4, column=2)





window.mainloop()