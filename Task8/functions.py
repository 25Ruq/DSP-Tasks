import math
import numpy as np
from Task1.signal import Signal
from Task8.CompareSignal import Compare_Signals


def calculate_correlation(guiobj):
    if guiobj.norm_option.get() == 0:
        result_signal = calculate_correlation_non(guiobj)
    else:
        result_signal = calculate_correlation_norm(guiobj)

    output_file = guiobj.outfile_text.get("1.0", "end-1c")
    result_signal.write_signal(output_file)
    Compare_Signals(guiobj.outfile_name, result_signal.indices, result_signal.samples)


def calculate_correlation_norm(guiobj):
    if len(guiobj.lst) == 1:
        first_signal = second_signal = guiobj.lst[0]
    elif len(guiobj.lst) == 2:
        first_signal = guiobj.lst[0]
        second_signal = guiobj.lst[1]
    else:
        print("Only 1 or 2 signals are allowed")
        return
    result = []
    count = first_signal.count
    squared_sum_1 = np.sum(first_signal.samples**2)
    squared_sum_2 = np.sum(second_signal.samples**2)
    for i in range(count):
        res = np.dot(first_signal.samples, second_signal.samples) / math.sqrt(squared_sum_1 * squared_sum_2)
        result.append(res)
        if second_signal.periodicity == 0:
            second_signal.samples = np.roll(second_signal.samples, -1)
            second_signal.samples[-1] = 0
            squared_sum_2 = np.sum(second_signal.samples ** 2)
        else:
            second_signal.samples = np.roll(second_signal.samples, -1)

    result_signal = Signal()
    result_signal.store_signal(second_signal.periodicity, 0, count, np.array(range(0, count, 1)), result)
    return result_signal



def calculate_correlation_non(guiobj):
    if len(guiobj.lst) == 1:
        first_signal = second_signal = guiobj.lst[0]
    elif len(guiobj.lst) == 2:
        first_signal = guiobj.lst[0]
        second_signal = guiobj.lst[1]
    else:
        print("Only 1 or 2 signals are allowed")
        return
    result = []
    count = first_signal.count
    for i in range(count):
        result.append(np.dot(first_signal.samples, second_signal.samples)/count)
        if second_signal.periodicity == 0:
            second_signal.samples = np.roll(second_signal.samples, -1)
            second_signal.samples[-1] = 0
        else:
            second_signal.samples = np.roll(second_signal.samples, -1)

    result_signal = Signal()
    result_signal.store_signal(second_signal.periodicity, 0, count, np.array(range(0, count, 1)), result)
    return result_signal
