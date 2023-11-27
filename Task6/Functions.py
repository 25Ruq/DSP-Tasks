from Task4.transformation import modify, transform
from Task5.comparesignal2 import *
import numpy as np


def moving_average(guiobj):
    if len(guiobj.lst) == 1:
        if guiobj.expected_signal is None:
            print("Select Expected Output File")
            return
        output_file = guiobj.outfile_text.get("1.0", "end-1c")
        if output_file == "":
            print("Enter Output File Name")
            return
        sig = guiobj.lst[0]
        signal_values = sig.samples

    smoothed_signal = []
    window_size = int(guiobj.num_text.get("1.0", "end-1c"))

    # Adjust range to start from window_size - 1 to ensure a full window
    for i in range(window_size - 1, len(signal_values)):
        window = signal_values[i - window_size + 1:i + 1]
        smoothed_signal.append(sum(window) / window_size)

    # Display the smoothed signal
    SignalSamplesAreEqual(guiobj.outfile_name, smoothed_signal)

def delay_signal(guiobj):
    sig = guiobj.lst[0]
    signal_values = sig.samples
    k = int(guiobj.num_text.get("1.0", "end-1c"))

    delayed_signal_indices = [i - k for i in range(len(signal_values))]
    delayed_signal_values = [signal_values[i] if i >= 0 else 0 for i in delayed_signal_indices]

    print("Indices:", delayed_signal_indices)
    print("Delayed Signal Values:", delayed_signal_values)

def advance_signal(guiobj):
    sig = guiobj.lst[0]
    signal_values = sig.samples
    k = int(guiobj.num_text.get("1.0", "end-1c"))

    advanced_signal_indices = [i + k for i in range(len(signal_values))]
    advanced_signal_values = [signal_values[i] if i < len(signal_values) else 0 for i in advanced_signal_indices]

    print("Indices:", advanced_signal_indices)
    print("Advanced Signal Values:", advanced_signal_values)

