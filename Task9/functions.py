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


def fast_convolution(guiobj):
    pass
