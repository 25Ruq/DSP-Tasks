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
