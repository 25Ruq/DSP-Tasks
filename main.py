from tkinter import *
from Task1.mainGUI import MainGUI
from Task2.GUI import Operations
from Task3.GUI import Quantization
from Task4.GUI import Transformation
from Task5.GUI import Components
from helper import open_task

root = Tk()
canvas = Canvas(root, width=400, height=300)
canvas.pack()

Button1 = Button(root, text="Task 1", command=lambda: open_task(root, MainGUI, "Task1"))
Button1.config(width=10)
canvas.create_window(200, 50, window=Button1)

Button2 = Button(root, text="Task 2", command=lambda: open_task(root, Operations, "Task2"))
Button2.config(width=10)
canvas.create_window(200, 100, window=Button2)

# select file instead of manually changing it
Button3 = Button(root, text="Task 3", command=lambda: open_task(root, Quantization, "Task3"))
Button3.config(width=10)
canvas.create_window(200, 150, window=Button3)

Button4 = Button(root, text="Task 4", command=lambda: open_task(root, Transformation, "Task4"))
Button4.config(width=10)
canvas.create_window(200, 200, window=Button4)

Button5 = Button(root, text="Task 5", command=lambda: open_task(root, Components, "Task5"))
Button5.config(width=10)
canvas.create_window(200, 250, window=Button5)

mainloop()
