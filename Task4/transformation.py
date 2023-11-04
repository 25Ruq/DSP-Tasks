import math
from Task1.signal import Signal
from Task4.signalcompare import *
from tkinter import END
import numpy as np


def euler(theta, p):
    theta = round(math.radians(theta), 3)
    return complex(round(math.cos(theta), 3) + p * round(math.sin(theta), 3))


def transform(guiobj):
    if len(guiobj.lst) == 1:
        sig = guiobj.lst[0]
        p = None
        op = guiobj.transformation_var.get()
        if op == "DFT" and sig.domain == 0:
            p = complex(0, -1)
        elif op == "IDFT" and sig.domain == 1:
            p = complex(0, 1)
        else:
            print("Signal type is incompatible with the operation")
            return
        try:
            ff = 2 * (22/7) * float(guiobj.sampling_freq_text.get("1.0", "end-1c")) / 4
        except ValueError:
            if op == "IDFT":
                ff = None
            else:
                print("Please Enter Sampling Frequency or change to IDFT")
                return
        amplitude = []
        shift = []
        ff_list = []
        N = sig.count
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
                amplitude.append(round(xk.real, 14))
            else:
                amplitude.append(round(math.sqrt((xk.real ** 2) + (xk.imag ** 2)), 14))
                shift.append(math.degrees(math.atan(xk.imag / xk.real)))
                ff_list.append(ff*(k+1))
        transformed_signal = Signal()
        if op == "DFT":
            try:
                index = int(guiobj.indexText.get("1.0", "end-1c"))
                amp = int(guiobj.ampText.get("1.0", "end-1c"))
                theta = int(guiobj.thetaText.get("1.0", "end-1c"))
                if modify(N, index, amp, theta, amplitude, shift) == 0:
                    return
            except ValueError:
                pass
            transformed_signal.store_signal(1 ^ int(sig.domain), sig.periodicity, N, amplitude, shift)
        elif op == "IDFT":
            amplitude.reverse()
            transformed_signal.store_signal(1 ^ int(sig.domain), sig.periodicity, N, np.array(range(0, N, 1)), amplitude)
        transformed_signal.write_signal(guiobj.outfile_text.get("1.0", "end-1c"))
        transformed_signal.plot_signals(ff_list)
        guiobj.lst.append(transformed_signal)
        guiobj.signals_listbox.insert(END, guiobj.outfile_text.get("1.0", "end-1c"))
    else:
        print("Too many signals, please keep one signal to transform")


def modify(N, index, amp, theta, amplitude, shift):
    if index >= 0 and index < N:
        amplitude[index] = amp
        shift[index] = theta
        return 1
    else:
        print("Modification FAILED : Index must be between 0 and", N-1)
        return 0
