from Task4.transformation import dft, idft
import numpy as np
import math
import cmath
from Task1.signal import Signal
from Task8.CompareSignal import Compare_Signals
from Task7.ConvTest import *

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
    conv_indices = np.arange(M) + sig1.indices[0] + sig2.indices[0]
    # Append zeros to both signals
    last_index1 = int(sig1.indices[-1]+1)
    last_index2 = int(sig2.indices[-1]+1)
    sig1.indices = np.append(sig1.indices, np.array(range(last_index1, M-last_index1, 1)))
    sig2.indices = np.append(sig2.indices, np.array(range(last_index2, M, 1)))
    sig1.count = M
    sig2.count = M
    sig1.samples = np.append(sig1.samples, np.zeros(M - N1))
    sig2.samples = np.append(sig2.samples, np.zeros(M - N2))

    # Perform DFT on both signals
    signal1_dft = dft(sig1)
    signal2_dft = dft(sig2)

    complex_first_signal = np.zeros(M, dtype=complex)
    complex_second_signal = np.zeros(M, dtype=complex)
    for i in range(M):
        complex_first_signal[i] = cmath.rect(signal1_dft.indices[i], signal1_dft.samples[i])
        complex_second_signal[i] = cmath.rect(signal2_dft.indices[i], signal2_dft.samples[i])

    # Multiply harmonics in the frequency domain
    product_result = complex_first_signal * complex_second_signal

    amp = []
    shift = []
    for i in range(M):
        shift.append(np.angle(product_result[i]))
        amp.append(math.sqrt((product_result[i].real ** 2) + (product_result[i].imag ** 2)))

    product_dft = Signal()
    product_dft.store_signal(1, 0, M, amp, shift)

    # Perform IDFT on the product signal
    product_signal = idft(product_dft)

    print(conv_indices)
    print(np.round(product_signal.samples, 1))
    ConvTest(conv_indices, product_signal.samples)
