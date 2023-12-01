from tkinter import *
from Task7.Convloution import *
from helper import select_signal, remove_signal ,remove_signal2 ,select_signal2

class Convlov:

    def __init__(self):
        self.expected_signal = None
        self.outfile_name = None
        self.lst = []
        self.lst2 = []
        self.root = Tk()
        self.root.geometry("400x400")

        self.input_label = Label(self.root, text="Input File x:")
        self.signals_listbox = Listbox(self.root, width=30, height=2)
        self.input_label.grid(row=0, column=0)
        self.signals_listbox.grid(row=0, column=1)

        self.select_input_button = Button(self.root, text="Select Input File", command=lambda: select_signal(self))
        self.select_input_button.config(width=25)
        self.select_input_button.grid(row=1, column=0)

        self.remove_input_button = Button(self.root, text="Remove Input File", command=lambda: remove_signal(self))
        self.remove_input_button.config(width=25)
        self.remove_input_button.grid(row=1, column=1)

        self.input_label = Label(self.root, text="Input File h:")
        self.signals_listbox = Listbox(self.root, width=30, height=2)
        self.input_label.grid(row=2, column=0)
        self.signals_listbox.grid(row=2, column=1)

        self.select_input_button = Button(self.root, text="Select Input File", command=lambda: select_signal2(self))
        self.select_input_button.config(width=25)
        self.select_input_button.grid(row=3, column=0)

        self.remove_input_button = Button(self.root, text="Remove Input File", command=lambda: remove_signal2(self))
        self.remove_input_button.config(width=25)
        self.remove_input_button.grid(row=3, column=1)

        # Create button to compute convolution
        self.convolve = Button(self.root, text="Compute Convolution", command=lambda: convolve(self))
        self.convolve.config(width=25)
        self.convolve.grid(row=4, column=1)

        mainloop()
