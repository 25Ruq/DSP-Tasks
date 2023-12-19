from tkinter import *
from helper import select_signal, remove_signal
from Task2.operations import *


class Operations:
    def __init__(self):
        self.lst = []
        self.root = Tk()
        self.root.geometry("400x400")

        # Create and configure the listbox for displaying signals
        self.signals_listbox = Listbox(self.root)
        self.signals_listbox.grid(row=0, column=1)

        # Create "Add Signal" button
        self.select_signal_button = Button(self.root, text="Select Signal", command=lambda: select_signal(self, 2))
        self.select_signal_button.grid(row=1, column=0)

        # Create a "Delete" button
        self.remove_signal_button = Button(self.root, text="Remove Signal", command=lambda: remove_signal(self))
        self.remove_signal_button.grid(row=1, column=1)

        # Create "Add" button
        self.add_button = Button(self.root, text="Add", command=lambda: calculate_result(self))
        self.add_button.grid(row=2, column=0)

        # Create "Subtract" button
        self.subtract_button = Button(self.root, text="Subtract", command=lambda: subtract_signals(self))
        self.subtract_button.grid(row=2, column=1)

        # Create "Multiply" button
        self.multiply_button = Button(self.root, text="Multiply", command=lambda: multiply_signal(self))
        self.multiply_button.grid(row=3, column=0)

        self.constantText = Text(self.root, height=2, width=20)
        self.constantText.grid(row=3, column=1)

        # Create "Square" button
        self.square_button = Button(self.root, text="Square", command=lambda: square_signal(self))
        self.square_button.grid(row=4, column=1)

        # Create a label for displaying the result signal
        self.result_label = Label(self.root, text="Result Signal:")
        self.result_label.grid(row=8, column=0)


        # 5
        self.shift_value = Text(self.root, height=2, width=15)
        self.shift_value.grid(row=5, column=0)
        self.shift_button = Button(self.root, text="Shift", command=lambda: shift(self))
        self.shift_button.config(width=10)
        self.shift_button.grid(row=5, column=1)

        # 6
        ranges = [
            "[0,1]",
            "[-1,1]"
        ]
        self.selected_range = StringVar(self.root)
        self.selected_range.set("Select Range")
        self.range_menu = OptionMenu(self.root, self.selected_range, *ranges)
        self.range_menu.config(width=15)
        self.range_menu.grid(row=6, column=1)
        self.normalize_button = Button(self.root, text="Normalize", command=lambda: norm(self))
        self.normalize_button.config(width=10)
        self.normalize_button.grid(row=6, column=0)

        # 7
        self.accumulate_button = Button(self.root, text="Accumulate", command=lambda: accumulate(self))
        self.accumulate_button.config(width=10)
        self.accumulate_button.grid(row=7, column=0)

        mainloop()
