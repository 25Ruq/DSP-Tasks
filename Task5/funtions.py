from Task4.transformation import modify, transform
from Task5.comparesignal2 import *
import numpy as np
def DCT():

    with open("DCT_input.txt", "r") as file:
        lines = file.readlines()
    signal_values = [float(line.split()[1]) for line in lines[3:]]
    N = len(signal_values)
    X = np.zeros(N)
    for k in range(N):
        sum_val = 0.0
        for n in range(N):
            sum_val += signal_values[n] * np.cos((np.pi / (4 * N)) * (2 * n - 1) * (2 * k - 1))
        X[k] = np.sqrt(2 / N) * sum_val

    m=int(input("Enter Coefficient :"))
    SignalSamplesAreEqual("DCT_output.txt",X)
    # Choose the first m coefficients
    selected_coefficients = X[:m]

    # Save selected coefficients to a text file
    np.savetxt("selected_coefficients.txt", selected_coefficients, fmt='%f', delimiter=', ',
               header=f"First {m} DCT coefficients")

    return X, selected_coefficients



def remove_DC(guiobj):
    transform(guiobj, 5)
    modify(guiobj.lst[0].count, 0, 0, 0, guiobj.lst[0])
    guiobj.transformation_var.set("IDFT")
    transform(guiobj, 5)
    SignalSamplesAreEqual(guiobj.outfile_name, guiobj.lst[0].samples)


computed_dct, selected = DCT()
#
#     # Print the selected coefficients
print(f"\nSelected  coefficients:")
print(selected)