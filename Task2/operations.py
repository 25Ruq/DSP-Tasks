from Task1.signal import Signal
import numpy as np
from itertools import zip_longest


def calculate_result(guiobj):
    signals = guiobj.lst
    if len(signals) > 1:
        signals = [signal.samples for signal in signals]
        # Perform element-wise addition of signals
        result_signal = [sum(x) for x in zip_longest(*signals, fillvalue=0)]

        guiobj.result_label.config(text="Add Result Signal: Ready")
        obj = Signal()
        obj.store_signal(0, 0, len(result_signal), range(0, len(result_signal)), result_signal)
        obj.plot_signals()
    else:
        guiobj.result_label.config(text="Add Result Signal: Not enough signals")


def subtract_signals(guiobj):
    signals = guiobj.lst
    if len(signals) >= 2:
        signals = [signal.samples for signal in signals]
        # Perform element-wise subtraction of signals
        result_signal = [x[0] - sum(x[1:]) for x in zip_longest(*signals, fillvalue=0)]

        guiobj.result_label.config(text="Subtract Result Signal: Ready")
        obj = Signal()
        obj.store_signal(0, 0, len(result_signal), range(0, len(result_signal)), result_signal)
        obj.plot_signals()
    else:
        guiobj.result_label.config(text="Subtract Result Signal: Not enough signals")


def multiply_signal(guiobj):
    constant = int(guiobj.constantText.get("1.0", "end-1c"))
    if guiobj.lst:
        obj = guiobj.lst[0]
        if constant == -1:
            result_signal = [x * -1 for x in obj.samples]  # Invert the signal
        else:
            result_signal = [x * constant for x in obj.samples]

        new_signal = Signal()
        new_signal.store_signal(0, 0, len(result_signal), range(0, len(result_signal)), result_signal)
        new_signal.plot_signals()


def square_signal(guiobj):
    if guiobj.lst:
        obj = guiobj.lst[0]
        result_signal = [x ** 2 for x in obj.samples]   # Square each element of the signal
        new_signal = Signal()
        new_signal.store_signal(0, 0, len(result_signal), range(0, len(result_signal)), result_signal)
        new_signal.plot_signals()


def shift(guiobj):
    if guiobj.lst:
        obj = guiobj.lst[0]
        val = int(guiobj.shift_value.get("1.0", "end-1c"))
        obj.indices = obj.indices - val
        obj.plot_signals()


def norm(guiobj):
    if guiobj.lst:
        obj = guiobj.lst[0]
        new_min = None
        new_max = None
        if guiobj.selected_range.get() == "[0,1]":
            new_min = 0
            new_max = 1
        elif guiobj.selected_range.get() == "[-1,1]":
            new_min = -1
            new_max = 1
        old_min = min(obj.samples)
        old_max = max(obj.samples)
        obj.samples = ((obj.samples-old_min)/(old_max-old_min))*(new_max-new_min)+new_min
        obj.plot_signals()


def accumulate(guiobj):
    if guiobj.lst:
        obj = guiobj.lst[0]
        for i in range(1, obj.count):
            obj.samples[i] = obj.samples[i] + obj.samples[i-1]
        obj.plot_signals()
