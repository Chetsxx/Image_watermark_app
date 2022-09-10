from tkinter import font
import tkinter as tk


class FontBox:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title('Font')
        self.root.geometry('500x500')
        self.font = font.Font(root=self.root, family="Helvetica", size=32)
        self.font_family = "Helvetica"
        self.font_sizing = "32"
        self.font_styling = "normal"
        self.input = None
        # Top Frame
        self.top_frame = tk.Frame(self.root, width=485, height=250)
        self.top_frame.pack(pady=10)



        #Bottom Frame
        self.bottom_frame = tk.Frame(self.root)
        self.bottom_frame.pack()

        # Freeze Frame
        self.top_frame.grid_propagate(False)
        self.top_frame.columnconfigure(0, weight=10)

        # Add Text box
        self.text = tk.Text(self.top_frame, font=self.font)
        self.text.insert(tk.INSERT, "Type Here")
        self.text.grid(row=0, column=0)
        self.text.grid_rowconfigure(0, weight=1)
        self.text.grid_columnconfigure(0, weight=1)

        # Add Label
        front_label = tk.Label(self.bottom_frame, text="Choose Font", font=("Helvetica", 10, "bold"))
        front_label.grid(row=0, column=0, padx=10, sticky=tk.W)

        size_label = tk.Label(self.bottom_frame, text="Choose Size", font=("Helvetica", 10, "bold"))
        size_label.grid(row=0, column=1, padx=10, sticky=tk.W)

        style_label = tk.Label(self.bottom_frame, text="Choose Style", font=("Helvetica", 10, "bold"))
        style_label.grid(row=0, column=2, padx=10, sticky=tk.W)

        # Add List Box
        # self.scroll = tk.Scrollbar(self.root, orient=tk.VERTICAL)
        # self.scroll.grid(row=1, column=0, sticky=tk.E)

        self.font_list = tk.Listbox(self.bottom_frame, selectmode=tk.SINGLE, width=35)
        self.font_list.grid(row=1, column=0, padx=10)



        # Add Fonts
        for f in font.families():
            self.font_list.insert('end', f)

        self.font_size = tk.Listbox(self.bottom_frame, selectmode=tk.SINGLE, width=15)
        self.font_size.grid(row=1, column=1, padx=10)

        font_sizes = [8, 10, 12, 16, 18, 36, 48]

        for s in font_sizes:
            self.font_size.insert('end', s)

        self.font_style = tk.Listbox(self.bottom_frame, selectmode=tk.SINGLE, width=20)
        self.font_style.grid(row=1, column=2, padx=10)

        font_styles = ["Regular", "Bold", "Italic"]

        for style in font_styles:
            self.font_style.insert("end", style)


        # Bind the listbox
        self.font_list.bind('<ButtonRelease-1>', self.font_chooser)
        self.font_size.bind('<ButtonRelease-1>', self.font_size_chooser)
        self.font_style.bind('<ButtonRelease-1>', self.font_style_chooser)

        self.add = tk.Button(self.bottom_frame, text="Add", command=self.text_box_input)
        self.add.grid(row=2, column=1, pady=10, padx=10, sticky=tk.E)


        self.root.mainloop()


    def font_chooser(self, event):
        self.font.config(family=self.font_list.get(self.font_list.curselection()))
        self.font_family = self.font_list.get(self.font_list.curselection())


    def font_size_chooser(self, event):
        self.font.config(size=self.font_size.get(self.font_size.curselection()))
        self.font_sizing = self.font_size.get(self.font_size.curselection())



    def font_style_chooser(self, event):
        style = self.font_style.get(self.font_style.curselection()).lower()

        if style == "bold":
            self.font.config(weight=style)
            self.font_styling == style
        elif style == "regular":
            self.font.config(weight="normal", slant='roman', underline=0, overstrike=0)
            self.font_styling == "normal"
        elif style == "italic":
            self.font.config(slant=style)
            self.font_styling == style


    def text_box_input(self):
        self.input = self.text.get("1.0", 'end-1c')
        self.root.quit()
















# from tkinter import *
#
#
#
#
# root = Tk()
# root.title('Watermarker')
# root.geometry("700x500")
#
# canvas = Canvas(root, bg="white", width=500, height=500)
# canvas.grid(row=0, column=0)
#
# font_style = Button(root, text='Pick a Font', command=font_chooser)
# font_style.grid(row=0, column=2, sticky=W)
#
#
# root.mainloop()
