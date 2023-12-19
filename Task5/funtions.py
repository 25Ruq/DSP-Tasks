from Task4.transformation import modify, dft, idft
from Task5.comparesignal2 import *
import numpy as np


def DCT(guiobj):
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
        N = len(signal_values)
        X = np.zeros(N)
        for k in range(N):
            sum_val = 0.0
            for n in range(N):
                sum_val += signal_values[n] * np.cos((np.pi / (4 * N)) * (2 * n - 1) * (2 * k - 1))
            X[k] = np.sqrt(2 / N) * sum_val

        m = int(guiobj.num_text.get("1.0", "end-1c"))
        SignalSamplesAreEqual(guiobj.outfile_name, X)

        # Choose the first m coefficients
        selected_coefficients = X[:m]

        # Save selected coefficients to a text file
        np.savetxt(output_file, selected_coefficients, fmt='%f', delimiter=', ',
                   header=f"First {m} DCT coefficients")


def remove_DC(guiobj):
    transformed_signal = dft(guiobj.lst[0])
    modify(transformed_signal.count, 0, 0, 0, transformed_signal)
    transformed_signal = idft(transformed_signal)
    transformed_signal.plot_signals()
    SignalSamplesAreEqual(guiobj.outfile_name, transformed_signal.samples)
