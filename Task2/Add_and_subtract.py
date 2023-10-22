import tkinter as tk
from tkinter import filedialog
import matplotlib.pyplot as plt
import numpy as np  # Added for subtraction

# Create an empty list to store the signals
signals = []

# Function to read signals from a text file
def read_signals(filename):
    signal = []
    with open(filename, 'r') as file:
        for line in file:
            # Split each line by whitespace and take the second column as the signal value
            signal_value = line.strip().split()
            if len(signal_value) >= 2:
                signal.append(float(signal_value[1]))
    return signal

# Function to handle the "Add Signal" button
def add_signal():
    file_path = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt")])
    if file_path:
        signal = read_signals(file_path)
        plot_signals(signal)
        signals.append(signal)
        update_signals_list()

# Function to handle the "Subtract Signals" button
def subtract_signals():
    if len(signals) >= 2:
        # Find the minimum length of signals
        min_length = min(len(signal) for signal in signals)

        # Perform element-wise subtraction of signals
        result_signal = np.zeros(min_length)
        for signal in signals:
            result_signal =np.abs(np.subtract(np.abs(result_signal), signal[:min_length]))

        result_label.config(text="Subtract Result Signal: Ready")
        plot_signals(result_signal)
    else:
        result_label.config(text="Subtract Result Signal: Not enough signals")
# Function to handle the "Calculate Result" button
def calculate_result():
    if len(signals) > 1:
        # Find the minimum length of signals
        min_length = min(len(signal) for signal in signals)

        # Perform element-wise addition of signals
        result_signal = [sum(signals[i][j] for i in range(len(signals))) for j in range(min_length)]

        result_label.config(text="Add Result Signal: Ready")
        plot_signals(result_signal)
    else:
        result_label.config(text="Add Result Signal: Not enough signals")

# Function to update the list of signals
def update_signals_list():
    signals_listbox.delete(0, tk.END)
    for i, signal in enumerate(signals):
        signals_listbox.insert(tk.END, f"Signal {i + 1}: {signal}")

# Function to plot analog and digital signals
def plot_signals(result_signal):
    plt.figure(figsize=(10, 6))

    # Plot the analog (continuous) signal
    plt.subplot(2, 1, 1)
    plt.plot(result_signal)
    plt.title("Analog Signal")
    plt.grid(True)

    # Plot the digital (discrete) signal
    plt.subplot(2, 1, 2)
    plt.stem(result_signal, basefmt=' ')
    plt.title("Digital Signal")
    plt.grid(True)

    plt.tight_layout()
    plt.show()

# Create the main root
root = tk.Tk()
root.geometry("350x320")
root.title("Signal Operations")

# Create and configure the listbox for displaying signals
signals_listbox = tk.Listbox(root)
signals_listbox.pack()

# Create "Add Signal" button
add_signal_button = tk.Button(root, text="Add Signal", command=add_signal)
add_signal_button.pack()

# Create "Calculate Result" button
calculate_result_button = tk.Button(root, text="Addition", command=calculate_result)
calculate_result_button.pack()

# Create "Subtract Signals" button
subtract_signals_button = tk.Button(root, text="Subtraction", command=subtract_signals)
subtract_signals_button.pack()

# Create a label for displaying the result signal
result_label = tk.Label(root, text="Result Signal:")
result_label.pack()

# Start the Tkinter main loop
root.mainloop()
