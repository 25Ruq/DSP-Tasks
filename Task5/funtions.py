from Task4.transformation import modify, transform
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
    transform(guiobj, 5)
    modify(guiobj.lst[0].count, 0, 0, 0, guiobj.lst[0])
    guiobj.transformation_var.set("IDFT")
    transform(guiobj, 5)
    guiobj.transformation_var.set("DFT")
    SignalSamplesAreEqual(guiobj.outfile_name, guiobj.lst[0].samples)
