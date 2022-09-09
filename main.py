from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from tkinter import colorchooser
from PIL import ImageTk, Image

color = "white"

def UploadAction(event=None):
    filename = filedialog.askopenfilename(title='open', filetype=(("jpeg", "*.jpg"), ("png", "*.png")))
    image_path = Image.open(filename)
    image_path = image_path.resize((700, 500), Image.ANTIALIAS)
    photo = ImageTk.PhotoImage(image_path)
    # image_label = Label(window, image=photo)
    # image_label.image = photo
    # image_label.grid(row=1, column=0, columnspan=2, rowspan=6, sticky=SW)
    canvas.create_image(0, 0, image=photo, anchor='nw')
    canvas.image = photo


def changes(event=None):
    pass

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

watermark_label = Label(window, text="Text", font=('calibre', 10,'normal'))
watermark_label.grid(row=2, column=1, padx=10, pady=10)

watermark_entry = Entry(window, font=('calibre', 10,'normal'), width=37)
watermark_entry.grid(row=2, column=2, columnspan=3, padx=10, pady=10)

font_label = Label(window, text="Font Size", font=('calibre', 10,'normal'))
font_label.grid(row=3, column=1, padx=10, pady=10)

font_entry = Entry(window, font=('calibre', 10,'normal'), width=37)
font_entry.grid(row=3, column=2, columnspan=3, padx=10, pady=10)

font_type_label = Label(window, text="Font", font=('calibre', 10,'normal'))
font_type_label.grid(row=4, column=1, padx=10, pady=10)

font_type_entry = Entry(window, font=('calibre', 10,'normal'), width=37)
font_type_entry.grid(row=4, column=2, columnspan=3, padx=10, pady=10)

add = Button(window, text='Add Changes', command=changes)
add.grid(row=5, column=2)

draw = Button(window, text='Pick a color', command=start_drawing)
draw.grid(row=6, column=2)





window.mainloop()