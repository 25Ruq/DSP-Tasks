from Task1.signal import Signal
from tkinter import END
import numpy as np
from Task4.signalcompare import *


def euler(theta, p):
    theta = math.radians(theta)
    return complex(math.cos(theta) + p * math.sin(theta))


def transform(guiobj, task=4):
    if len(guiobj.lst) == 1:
        if guiobj.expected_signal is None:
            print("Select Expected Output File")
            return
        output_file = guiobj.outfile_text.get("1.0", "end-1c")
        if output_file == "":
            print("Enter Output File Name")
            return
        sig = guiobj.lst[0]
        N = sig.count
        op = guiobj.transformation_var.get()
        if op == "DFT" and sig.domain == 0:
            p = complex(0, -1)
        elif op == "IDFT" and sig.domain == 1:
            if task == 4:
                try:
                    index = int(guiobj.indexText.get("1.0", "end-1c"))
                    amp = None
                    theta = None
                    try:
                        amp = float(guiobj.ampText.get("1.0", "end-1c"))
                        theta = float(guiobj.thetaText.get("1.0", "end-1c"))
                    except ValueError:
                        pass
                    modify(N, index, amp, theta, sig)
                except ValueError:
                    pass
            p = complex(0, 1)
        else:
            print("Signal type is incompatible with the operation")
            return
        amplitude = []
        shift = []
        ff_list = []
        if task == 4:
            try:
                ff = 2 * (22/7) * float(guiobj.sampling_freq_text.get("1.0", "end-1c")) / N
            except ValueError:
                if op == "IDFT":
                    ff = None
                else:
                    print("Please Enter Sampling Frequency or change to IDFT")
                    return

        for k in range(N):
            xk = complex(0, 0)
            for n in range(N):
                if k == 0 or n == 0:
                    x = complex(sig.samples[n])
                    xk += x
                else:
                    x = complex(sig.samples[n] * euler(360*n*k/N, p))
                    xk += x
            if op == "IDFT":
                xk /= N
                amplitude.append(xk.real)
            else:
                # amplitude.append(np.round(math.sqrt((xk.real ** 2) + (xk.imag ** 2)), 13))
                amplitude.append(math.sqrt((xk.real ** 2) + (xk.imag ** 2)))
                shift.append(np.angle(xk))
                if task == 4:
                    ff_list.append(ff*(k+1))
        transformed_signal = Signal()
        if op == "DFT":
            transformed_signal.store_signal(sig.periodicity, 1 ^ int(sig.domain), N, amplitude, shift)
        elif op == "IDFT":
            transformed_signal.store_signal(sig.periodicity, 1 ^ int(sig.domain), N, np.array(range(0, N, 1)), amplitude)
        transformed_signal.write_signal(output_file)
        transformed_signal.plot_signals(ff_list)
        if task == 4:
            if test(guiobj.expected_signal, transformed_signal, op):
                print("TEST PASSED")
            else:
                print("TEST FAILED")
        transformed_signal = Signal()
        transformed_signal.read_signal(output_file)
        guiobj.lst.pop()
        guiobj.signals_listbox.delete(0, END)
        guiobj.lst.append(transformed_signal)
        guiobj.signals_listbox.insert(END, output_file)
    elif len(guiobj.lst) < 1:
        print("No signal selected, please select one signal to transform")

def modify(N, index, amp, theta, sig):
    if index >= 0 and index < N:
        if amp is None and theta is None:
            print("Modification FAILED: Enter Amplitude or Phase Shift values, or empty index text box")
        else:
            sig.samples[index] = complex(amp * math.cos(theta), amp * math.sin(theta))
    else:
        print("Modification FAILED: Index must be between 0 and", N-1)


def test(expected_signal, my_signal, op):
    if op == "DFT":
        return (SignalComapreAmplitude(my_signal.indices, expected_signal.indices)
                and SignalComaprePhaseShift(my_signal.samples, my_signal.samples))
    elif op == "IDFT":
        return SignalComapreAmplitude(my_signal.samples, expected_signal.samples)
