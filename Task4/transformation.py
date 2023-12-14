from Task1.signal import Signal
import cmath
import numpy as np
from Task4.signalcompare import *


def transform(guiobj):
    sig = guiobj.lst[0]
    op = guiobj.transformation_var.get()
    if op == "DFT":
        sampling_freq = float(guiobj.sampling_freq_text.get("1.0", "end-1c"))
        ff = 2 * (22 / 7) * sampling_freq / sig.count
        ff_list = list(ff*np.array(range(1, sig.count+1, 1)))
        transformed_signal = dft(sig)
        transformed_signal.plot_signals(ff_list)
    else:
        try:
            index = int(guiobj.indexText.get("1.0", "end-1c"))
            amp = float(guiobj.ampText.get("1.0", "end-1c"))
            theta = float(guiobj.thetaText.get("1.0", "end-1c"))
            modify(sig.count, index, amp, theta, sig)
        except ValueError:
            pass
        transformed_signal = idft(sig)
        transformed_signal.plot_signals()
    output_file = guiobj.outfile_text.get("1.0", "end-1c")
    transformed_signal.write_signal(output_file)
    if test(guiobj.expected_signal, transformed_signal, op):
        print("TEST PASSED")
    else:
        print("TEST FAILED")


def dft(sig):
    N = sig.count
    x = np.zeros(N, dtype=complex)
    amplitude = []
    shift = []
    for k in range(N):
        for n in range(N):
            if k == 0 or n == 0:
                x[k] += sig.samples[n]
            else:
                x[k] += sig.samples[n] * np.exp(-2j*math.pi*n*k/N)
        shift.append(np.angle(x[k]))
        amplitude.append(math.sqrt((x[k].real ** 2) + (x[k].imag ** 2)))
    transformed_signal = Signal()
    transformed_signal.store_signal(1 ^ int(sig.domain), sig.periodicity, N, amplitude, shift)
    return transformed_signal


def idft(sig):
    N = sig.count
    values = np.zeros(N, dtype=complex)
    for i in range(N):
        real = sig.indices[i] * math.cos(sig.samples[i])
        imag = sig.indices[i] * math.sin(sig.samples[i])
        values[i] = complex(real, imag)
    x = np.zeros(N, dtype=complex)
    amplitude = []
    for k in range(N):
        for n in range(N):
            if k == 0 or n == 0:
                x[k] += values[n]
            else:
                x[k] += values[n] * np.exp(2j * math.pi * n * k / N)
        x[k] /= N
        amplitude.append(x[k].real)
    transformed_signal = Signal()
    transformed_signal.store_signal(1 ^ int(sig.domain), sig.periodicity, N, np.array(range(0, N, 1)), amplitude)
    return transformed_signal


def modify(N, index, amp, theta, sig):
    if index >= 0 and index < N:
        if amp is None and theta is None:
            print("Modification FAILED: Enter Amplitude or Phase Shift values, or empty index text box")
        else:
            sig.indices[index] = amp
            sig.samples[index] = theta
    else:
        print("Modification FAILED: Index must be between 0 and", N-1)


def test(expected_signal, my_signal, op):
    if op == "DFT":
        return (SignalComapreAmplitude(my_signal.indices, expected_signal.indices)
                and SignalComaprePhaseShift(my_signal.samples, my_signal.samples))
    elif op == "IDFT":
        return SignalComapreAmplitude(my_signal.samples, expected_signal.samples)