from tkinter import *
from helper import open_task
from Task1.generateGUI import GenerateGUI
from Task1.readanddisplay import read_display


class MainGUI:
    def __init__(self):
        root = Tk()
        canvas = Canvas(root, width=400, height=300)
        canvas.pack()

        Button1 = Button(root, text="Generate wave",command=lambda: open_task(root, GenerateGUI, "Signals"))
        Button1.config(width=15)
        canvas.create_window(200, 50, window=Button1)

        Button2 = Button(root, text="Read Signal", command=lambda: read_display())
        Button2.config(width=10)
        canvas.create_window(200, 100, window=Button2)
        mainloop()
