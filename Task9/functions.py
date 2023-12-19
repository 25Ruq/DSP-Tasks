from Task4.transformation import dft, idft
import numpy as np
import math
import cmath
from Task1.signal import Signal
from Task8.CompareSignal import Compare_Signals


def fast_correlation(guiobj):
    if len(guiobj.lst) == 1:
        first_signal = second_signal = guiobj.lst[0]
    elif len(guiobj.lst) == 2:
        first_signal = guiobj.lst[0]
        second_signal = guiobj.lst[1]
    else:
        print("Only 1 or 2 signals are allowed")
        return
    print(first_signal)
    first_signal = dft(first_signal)
    second_signal = dft(second_signal)
    N = first_signal.count
    complex_first_signal = np.zeros(N, dtype=complex)
    complex_second_signal = np.zeros(N, dtype=complex)
    for i in range(N):
        complex_first_signal[i] = cmath.rect(first_signal.indices[i], first_signal.samples[i])
        complex_second_signal[i] = cmath.rect(second_signal.indices[i], second_signal.samples[i])
    complex_first_signal = np.conjugate(complex_first_signal)
    multiply = complex_first_signal * complex_second_signal
    amp = []
    shift = []
    for i in range(N):
        shift.append(np.angle(multiply[i]))
        amp.append(math.sqrt((multiply[i].real ** 2) + (multiply[i].imag ** 2)))
    result_signal = Signal()
    result_signal.store_signal(1, second_signal.periodicity, N, amp, shift)
    result_signal = idft(result_signal)
    result_signal.samples[:] = [x / N for x in result_signal.samples]
    Compare_Signals(guiobj.outfile_name, result_signal.indices, result_signal.samples)


# Function to calculate the frequency domain indices

def fast_convolution(guiobj):
    if len(guiobj.lst) == 1:
        sig1 = sig2 = guiobj.lst[0]
    elif len(guiobj.lst) == 2:
        sig1 = guiobj.lst[0]
        sig2 = guiobj.lst[1]
    else:
        print("Only 1 or 2 signals are allowed")
        return

    N1 = sig1.count
    N2 = sig2.count
    M = N1+N2-1

    # Append zeros to both signals
    sig1.samples = np.append(sig1.samples , np.zeros(M - N1))
    sig2.samples = np.append(sig2.samples , np.zeros(M - N2))

    # Perform DFT on both signals
    signal1_dft = dft(sig1)
    signal2_dft = dft(sig2)

    # Multiply harmonics in the frequency domain
    product_dft = Signal()
    product_dft.store_signal(1, 0, M, np.array(range(0, M, 1)),sig2.samples)

    # Make sure that the arrays have the same length by appending zeros if necessary
    if len(signal1_dft.samples) < len(signal2_dft.samples):
        signal1_dft.samples = np.append(signal1_dft.samples, np.zeros(len(signal2_dft.samples) - len(signal1_dft.samples)))
    elif len(signal2_dft.samples) < len(signal1_dft.samples):
        signal2_dft.samples = np.append(signal2_dft.samples, np.zeros(len(signal1_dft.samples) - len(signal2_dft.samples)))

    product_dft.samples = np.array(signal1_dft.samples) * np.array(signal2_dft.samples)

    # Perform IDFT on the product signal
    product_signal = idft(product_dft)

    print(product_signal.samples)