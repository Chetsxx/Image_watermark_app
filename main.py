from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from tkinter import colorchooser
from tkinter import font
from PIL import ImageTk, Image
from fonts import FontBox
from PIL import ImageGrab

color = "black"

def UploadAction(event=None):
    global img_name
    filename = filedialog.askopenfilename(title='open', filetype=(("jpeg", "*.jpg"), ("png", "*.png")))
    image_path = Image.open(filename)
    image_path = image_path.resize((700, 500), Image.ANTIALIAS)
    img_name = filename.split('/')[-1]
    img_name = img_name[0:-4]
    photo = ImageTk.PhotoImage(image_path)
    canvas.create_image(0, 0, image=photo, anchor='nw')
    canvas.image = photo

def font_chooser():
    global text_on_image
    fontbox = FontBox()
    text_on_image = canvas.create_text(50, 50, text=fontbox.input, font=(fontbox.font_family, fontbox.font_sizing, fontbox.font_styling))

def start_drawing():
    global color
    color = colorchooser.askcolor()[1]

    try:
        canvas.itemconfig(text_on_image, fill=color)
    except NameError:
        pass

def delete_last():
   canvas.delete(text_on_image)

def delete():
    canvas.delete("all")

def getx_gety(event):
    global lasx, lasy
    lasx, lasy = event.x, event.y

def draw(event):
    global lasx, lasy
    global color
    global line
    canvas.create_line((lasx, lasy, event.x, event.y), fill=color, width=1)
    lasx, lasy = event.x, event.y

def position():
    x_cod = float(x_entry.get())
    y_cod = float(y_entry.get())
    angles = float(angle_entry.get())
    canvas.itemconfig(text_on_image, fill=color, angle=angles)

    canvas.moveto(text_on_image, x_cod, y_cod)

def save_pic():
    global img_name
    x = window.winfo_rootx() + canvas.winfo_x()
    y = window.winfo_rooty() + canvas.winfo_y()
    x1 = x + canvas.winfo_width()
    y1 = y + canvas.winfo_height()

    try:
        new_name = img_name + 'new_watermarked.jpg'
    except NameError:
        new_name = 'new_watermarked.jpg'

    file_location = filedialog.askdirectory(title="Save new images to...")
    image = ImageGrab.grab(bbox=(x, y, x1, y1))
    image.save(f"{file_location}/{new_name}")

window = Tk()
window.title('Watermarker')
window.geometry("700x500")
window.resizable(True, True)
window.config(padx=50, pady=50)
window.grid_rowconfigure(0, weight=1)
window.grid_columnconfigure(0, weight=1)

size = ttk.Sizegrip(window)
size.grid(row=1, sticky=SW)

title = Label(text="Image Watermarker", font=("Ariel", 24, "bold"), fg="blue")
title.grid(row=0, column=0, columnspan=3)

canvas = Canvas(window, bg="white", width=700, height=500)
canvas.grid(row=1, column=0, columnspan=1, rowspan=9, sticky=NW, padx=10, pady=10)
canvas.bind("<Button-1>", getx_gety)
canvas.bind("<B1-Motion>", draw)

open_img = Button(window, text='Open Image', command=UploadAction)
open_img.grid(row=1, column=2, sticky=W)

font_style = Button(window, text='Pick a Font', command=font_chooser)
font_style.grid(row=3, column=2, sticky=W)

x_label = Label(window, text='X', font=("bold"))
x_label.grid(row=4, column=2, sticky=W)

x_entry = Entry(window)
x_entry.insert(END, 50)
x_entry.grid(row=4, column=3, sticky=W)

y_label = Label(window, text='Y', font=("bold"))
y_label.grid(row=5, column=2, sticky=W)

y_entry = Entry(window)
y_entry.insert(END, 50)
y_entry.grid(row=5, column=3, sticky=W)

angle_label = Label(window, text='Angle', font=("bold"))
angle_label.grid(row=6, column=2, sticky=W)

angle_entry = Entry(window)
angle_entry.insert(END, 360)
angle_entry.grid(row=6, column=3, sticky=W)

cords = Button(window, text='Change coordinates and angle', command=position)
cords.grid(row=7, column=2, sticky=W)

draw = Button(window, text='Pick a color', command=start_drawing)
draw.grid(row=8, column=2, sticky=W)

delete_btn = Button(text="Undo Text", command=delete_last)
delete_btn.grid(row=9, column=2, sticky=W)

save = Button(text='Save Image', command=save_pic)
save.grid(row=10, column=2, sticky=W)

window.mainloop()