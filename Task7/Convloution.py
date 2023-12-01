from tkinter import messagebox
import matplotlib.pyplot as plt
from tkinter import END
import numpy as np


def convolve(guiobj):
    sig1 = guiobj.lst[0]
    signal_values1 = np.array(sig1.samples)
    signal_indices1 = np.array(sig1.indices)
    sig2 = guiobj.lst2[0]
    signal_values2 = np.array(sig2.samples)
    signal_indices2 = np.array(sig2.indices)

    # Lengths of input sequences
    len_x = len(signal_values1)
    len_h = len(signal_values2)

    # Initialize result y with zeros
    y = [0] * (len_x + len_h - 1)
    conv_indices = np.arange(len_x + len_h - 1) + signal_indices1[0] + signal_indices2[0]

    # Perform convolution
    for n in range(len_x):
        for k in range(len_h):
            y[n + k] += signal_values1[n] * signal_values2[k]

    # Plotting the signals and convolution result
    plt.figure(figsize=(10, 5))

    plt.subplot(3, 1, 1)
    plt.stem(signal_indices1, signal_values1, label='x[n]')
    plt.legend()

    plt.subplot(3, 1, 2)
    plt.stem(signal_indices2, signal_values2, label='h[n]')
    plt.legend()

    plt.subplot(3, 1, 3)
    plt.stem(conv_indices, y, label='y[n] = x[n] * h[n]')
    plt.legend()

    plt.tight_layout()
    plt.show()

    print("the y(n) = [", y, "]")
    print("Indices after convolution:", list(conv_indices))
