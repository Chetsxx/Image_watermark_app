from tkinter import font
import tkinter as tk


class FontBox:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title('Font')
        self.window.geometry('500x500')
        self.font = font.Font(family="Helvetica", size=32)

        self.frame = tk.Frame(self.window, width=480, height=275)
        self.frame.pack(pady=10)

        # Freeze Frame
        self.frame.grid_propagate(False)
        self.frame.columnconfigure(0, weight=10)

        # Add Text box
        self.text = tk.Text(self.frame, font=self.font)
        self.text.grid(row=0, column=0)
        self.text.grid_rowconfigure(0, weight=1)
        self.text.grid_columnconfigure(0, weight=1)

        self.scroll = tk.Scrollbar(self.window, orient=tk.VERTICAL)
        self.scroll.pack(side=tk.RIGHT, fill="y")

        # Add List Box
        self.list = tk.Listbox(self.window, selectmode=tk.SINGLE, width=80, yscrollcommand=self.scroll.set)
        self.list.pack(side=tk.LEFT, fill="both")

        self.scroll.configure(command=self.list.yview)

        # Add Fonts
        for f in font.families():
            self.list.insert('end', f)



        self.window.mainloop()


fontbox = FontBox()



