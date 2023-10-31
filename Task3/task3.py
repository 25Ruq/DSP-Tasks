import tkinter as tk
import matplotlib as plt
from tkinter import ttk
import numpy as np
import math

def quantize_signal():
    # Read the signal from the file
    with open("Quan2_input.txt", "r") as file:
        lines = file.readlines()
    signal_values = [float(line.split()[1]) for line in lines[3:]]

    # Clear previous results
    encoded_list.delete(0, tk.END)
    quantized_list.delete(0, tk.END)
    interval_list.delete(0, tk.END)
    error_interval_list.delete(0, tk.END)

    # Get the user's choice (bits or levels)
    if bits_radio_var.get() == 1:
        num_bits_str = num_bits_entry.get()
        num_bits = int(num_bits_str)
        num_levels = 2 ** num_bits
    else:
        num_levels_str = num_levels_entry.get()
        if not num_levels_str.strip():
            avg_error_label.config(text="Invalid input. Please enter a valid number of levels.")
            return
        num_levels = int(num_levels_str)
        if num_levels <= 0:
            avg_error_label.config(text="Invalid input. Number of levels must be greater than 0.")
            return
        num_bits = int(math.ceil(math.log2(num_levels)))

    # Quantization
    min_amp = min(signal_values)
    max_amp = max(signal_values)
    delta = (max_amp - min_amp) / num_levels
    # Calculate the range values with possible duplicates
    quantization_ranges = [min_amp + i * delta for i in range(num_levels)]
    quantized_signal = []

    for value in signal_values:
        quantized_value = None
        for i, r in enumerate(quantization_ranges):
            if r <= value <= r + delta:
                quantized_value = i
                break
        quantized_signal.append(quantized_value)

    encoded_values = []
    quantized_values=[]
    error_list=[]
    # Display quantized signal and error
    for i, quantized_value in enumerate(quantized_signal):
        if quantized_value is not None:
            encoded_list.insert(tk.END, format(quantized_value, f'0{num_bits}b'))
            quantized_list.insert(tk.END, round(quantization_ranges[quantized_value] + delta / 2, 2))
            if bits_radio_var.get() == 0:
                midpoint = quantization_ranges[quantized_value] + delta / 2
                error = midpoint - signal_values[i]
                error_interval_list.insert(tk.END, round(error, 3))
                error_list.append(round(error, 3))
            needed=quantized_value
        else:

            encoded_list.insert(tk.END, format(needed, f'0{num_bits}b'))
            encoded_values.append(format(needed, f'0{num_bits}b'))
            quantized_list.insert(tk.END, round(quantization_ranges[needed] + delta / 2, 2))
            if bits_radio_var.get() == 0:
                midpoint = quantization_ranges[needed] + delta / 2
                error = midpoint - signal_values[i]
                error_interval_list.insert(tk.END, round(error, 3))
                error_list.append(round(error, 3))

        encoded_values.append(str(i))
        quantized_values.append(round(quantization_ranges[needed] + delta / 2, 2))

    if bits_radio_var.get() == 0:  # Create a list to store the interval indices
        interval_indices = []
        # Calculate and store the interval indices for each sample
        for value in signal_values:
            for i, r in enumerate(quantization_ranges ):
                if r <= value <= math.ceil(r + delta):
                    interval_indices.append(i+1)  # Add 1 to match your desired indexing
                    break

        # Display interval indices in the interval_list
        for index in interval_indices:
            interval_list.insert(tk.END, index)



    QuantizationTest2("Quan2_input.txt",interval_indices,encoded_values,quantized_values,error_list)


def QuantizationTest2(file_name, Your_IntervalIndices, Your_EncodedValues, Your_QuantizedValues, Your_SampledError):
    expectedIntervalIndices = []
    expectedEncodedValues = []
    expectedQuantizedValues = []
    expectedSampledError = []
    with open(file_name, 'r') as f:
        line = f.readline()
        line = f.readline()
        line = f.readline()
        line = f.readline()
        while line:
            # process line
            L = line.strip()
            if len(L.split(' ')) == 4:
                L = line.split(' ')
                V1 = int(L[0])
                V2 = str(L[1])
                V3 = float(L[2])
                V4 = float(L[3])
                expectedIntervalIndices.append(V1)
                expectedEncodedValues.append(V2)
                expectedQuantizedValues.append(V3)
                expectedSampledError.append(V4)
                line = f.readline()
            else:
                break
    if (len(Your_IntervalIndices) != len(expectedIntervalIndices)
            or len(Your_EncodedValues) != len(expectedEncodedValues)
            or len(Your_QuantizedValues) != len(expectedQuantizedValues)
            or len(Your_SampledError) != len(expectedSampledError)):
        print(Your_IntervalIndices)
        print(expectedIntervalIndices)
        print("QuantizationTest2 Test case failed, your signal have different length from the expected one")
        return
    for i in range(len(Your_IntervalIndices)):
        if (Your_IntervalIndices[i] != expectedIntervalIndices[i]):
            print("QuantizationTest2 Test case failed, your signal have different indicies from the expected one")
            return
    for i in range(len(Your_EncodedValues)):
        if (Your_EncodedValues[i] != expectedEncodedValues[i]):
            print(
                "QuantizationTest2 Test case failed, your EncodedValues have different EncodedValues from the expected one")
            return

    for i in range(len(expectedQuantizedValues)):
        if abs(Your_QuantizedValues[i] - expectedQuantizedValues[i]) < 0.01:
            continue
        else:
            print(
                "QuantizationTest2 Test case failed, your QuantizedValues have different values from the expected one")
            return
    for i in range(len(expectedSampledError)):
        if abs(Your_SampledError[i] - expectedSampledError[i]) < 0.01:
            continue
        else:
            print("QuantizationTest2 Test case failed, your SampledError have different values from the expected one")
            return
    print("QuantizationTest2 Test case passed successfully")

# Create the main window
root = tk.Tk()
root.title("Signal Quantization")

# Create and configure the GUI components
bits_radio_var = tk.IntVar()
bits_radio = ttk.Radiobutton(root, text="Enter Number of Bits:", variable=bits_radio_var, value=1)
bits_radio.grid(row=0, column=0)
num_bits_entry = ttk.Entry(root)
num_bits_entry.grid(row=0, column=1)
bits_radio_var.set(1)

levels_radio = ttk.Radiobutton(root, text="Enter Number of Levels:", variable=bits_radio_var, value=0)
levels_radio.grid(row=1, column=0)
num_levels_entry = ttk.Entry(root)
num_levels_entry.grid(row=1, column=1)

quantize_button = ttk.Button(root, text="Quantize Signal", command=quantize_signal)
quantize_button.grid(row=2, columnspan=2)

encoded_list = tk.Listbox(root)
encoded_list.grid(row=3, column=0)
quantized_list = tk.Listbox(root)
quantized_list.grid(row=3, column=1)

interval_list = tk.Listbox(root)
interval_list.grid(row=4, column=0)
error_interval_list = tk.Listbox(root)
error_interval_list.grid(row=4, column=1)

avg_error_label = ttk.Label(root, text="")
avg_error_label.grid(row=5, columnspan=2)

# Start the GUI main loop
root.mainloop()
