import tkinter as tk
from tkinter import ttk
from Task3.quantization import quantize_signal

# Create the main window
class Quantization:

    def __init__(self):
        root = tk.Tk()
        root.title("Signal Quantization")

        # Create and configure the GUI components
        self.bits_radio_var = tk.IntVar(root)
        self.bits_radio = ttk.Radiobutton(root, text="Enter Number of Bits:", variable=self.bits_radio_var, value=1)
        self.bits_radio.grid(row=0, column=0)
        self.num_bits_entry = ttk.Entry(root)
        self.num_bits_entry.grid(row=0, column=1)
        self.bits_radio_var.set(1)

        self.levels_radio = ttk.Radiobutton(root, text="Enter Number of Levels:", variable=self.bits_radio_var, value=0)
        self.levels_radio.grid(row=1, column=0)
        self.num_levels_entry = ttk.Entry(root)
        self.num_levels_entry.grid(row=1, column=1)

        self.quantize_button = ttk.Button(root, text="Quantize Signal", command=lambda: quantize_signal(self))
        self.quantize_button.grid(row=2, columnspan=2)

        self.encoded_list = tk.Listbox(root)
        self.encoded_list.grid(row=3, column=0)
        self.quantized_list = tk.Listbox(root)
        self.quantized_list.grid(row=3, column=1)

        self.interval_list = tk.Listbox(root)
        self.interval_list.grid(row=4, column=0)
        self.error_interval_list = tk.Listbox(root)
        self.error_interval_list.grid(row=4, column=1)

        self.avg_error_label = ttk.Label(root, text="")
        self.avg_error_label.grid(row=5, columnspan=2)

        # Start the GUI main loop
        root.mainloop()
