from tkinter import *
from helper import select_signal, remove_signal
from Task8.functions import *


class Correlation:
    def __init__(self):
        self.expected_signal = None
        self.outfile_name = None
        self.lst = []
        self.root = Tk()
        self.root.geometry("400x400")

        self.input_label = Label(self.root, text="Input File:")
        self.signals_listbox = Listbox(self.root, width=30, height=2)
        self.input_label.grid(row=0, column=0)
        self.signals_listbox.grid(row=0, column=1)

        self.select_input_button = Button(self.root, text="Select Input File", command=lambda: select_signal(self, 2))
        self.select_input_button.config(width=25)
        self.select_input_button.grid(row=1, column=0)

        self.remove_input_button = Button(self.root, text="Remove Input File", command=lambda: remove_signal(self))
        self.remove_input_button.config(width=25)
        self.remove_input_button.grid(row=1, column=1)

        self.outfile_label = Label(self.root, text="Output File:")
        self.outfile_text = Text(self.root, height=2, width=22)
        self.outfile_label.grid(row=2, column=0)
        self.outfile_text.grid(row=2, column=1)

        self.expected_outfile_label = Label(self.root, text="Expected Output File:")
        self.expected_signals_listbox = Listbox(self.root, width=30, height=2)
        self.expected_outfile_label.grid(row=3, column=0)
        self.expected_signals_listbox.grid(row=3, column=1)

        self.select_output_button = Button(self.root, text="Select Expected Output File", command=lambda: select_signal(self, 1))
        self.select_output_button.config(width=25)
        self.select_output_button.grid(row=4, column=0)

        self.remove_output_button = Button(self.root, text="Remove Expected Output File", command=lambda: remove_signal(self, 1))
        self.remove_output_button.config(width=25)
        self.remove_output_button.grid(row=4, column=1)

        self.norm_option = IntVar(self.root)
        self.norm_option.set(0)
        self.normalized_corr = Radiobutton(self.root, text="Normalized", variable=self.norm_option, value=1)
        self.normalized_corr.grid(row=5, column=0)
        self.non_normalized_corr = Radiobutton(self.root, text="Non Normalized", variable=self.norm_option, value=0)
        self.non_normalized_corr.grid(row=5, column=1)

        self.corr_button = Button(self.root, text="Calculate Correlation", command=lambda: calculate_correlation(self))
        self.corr_button.config(width=25)
        self.corr_button.grid(row=6, column=0)

        mainloop()