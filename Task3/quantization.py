import tkinter as tk
import math


def quantize_signal(guiobj):
    # Read the signal from the file
    with open("Quan1_input.txt", "r") as file:
        lines = file.readlines()
    signal_values = [float(line.split()[1]) for line in lines[3:]]

    # Clear previous results
    guiobj.encoded_list.delete(0, tk.END)
    guiobj.quantized_list.delete(0, tk.END)
    guiobj.interval_list.delete(0, tk.END)
    guiobj.error_interval_list.delete(0, tk.END)

    # Get the user's choice (bits or levels)
    if guiobj.bits_radio_var.get() == 1:
        num_bits_str = guiobj.num_bits_entry.get()
        num_bits = int(num_bits_str)
        num_levels = 2 ** num_bits
    else:
        num_levels_str = guiobj.num_levels_entry.get()
        if not num_levels_str.strip():
            guiobj.avg_error_label.config(text="Invalid input. Please enter a valid number of levels.")
            return
        num_levels = int(num_levels_str)
        if num_levels <= 0:
            guiobj.avg_error_label.config(text="Invalid input. Number of levels must be greater than 0.")
            return
        num_bits = int(math.ceil(math.log2(num_levels)))

    # Quantization
    min_amp = min(signal_values)
    max_amp = max(signal_values)
    delta = (max_amp - min_amp) / num_levels
    # Calculate the range values with possible duplicates
    quantization_ranges = [min_amp + i * delta for i in range(num_levels)]
    quantized_signal = []

    for value in signal_values:
        quantized_value = None
        for i, r in enumerate(quantization_ranges):
            if r <= value <= r + delta:
                quantized_value = i
                break
        quantized_signal.append(quantized_value)

    encoded_values = []
    quantized_values = []
    error_list = []
    # Display quantized signal and error
    for i, quantized_value in enumerate(quantized_signal):
        if quantized_value is not None:
            guiobj.encoded_list.insert(tk.END, format(quantized_value, f'0{num_bits}b'))
            encoded_values.append(format(quantized_value, f'0{num_bits}b'))
            guiobj.quantized_list.insert(tk.END, round(quantization_ranges[quantized_value] + delta / 2, 2))
            if guiobj.bits_radio_var.get() == 0:
                midpoint = quantization_ranges[quantized_value] + delta / 2
                error = midpoint - signal_values[i]
                guiobj.error_interval_list.insert(tk.END, round(error, 3))
                error_list.append(round(error, 3))
            needed = quantized_value
        else:
            guiobj.encoded_list.insert(tk.END, format(needed, f'0{num_bits}b'))
            encoded_values.append(format(needed, f'0{num_bits}b'))
            guiobj.quantized_list.insert(tk.END, round(quantization_ranges[needed] + delta / 2, 2))
            if guiobj.bits_radio_var.get() == 0:
                midpoint = quantization_ranges[needed] + delta / 2
                error = midpoint - signal_values[i]
                guiobj.error_interval_list.insert(tk.END, round(error, 3))
                error_list.append(round(error, 3))

        quantized_values.append(round(quantization_ranges[needed] + delta / 2, 2))

    if guiobj.bits_radio_var.get() == 0:  # Create a list to store the interval indices
        interval_indices = []
        # Calculate and store the interval indices for each sample
        for value in signal_values:
            for i, r in enumerate(quantization_ranges):
                if r <= value <= math.ceil(r + delta):
                    interval_indices.append(i+1)  # Add 1 to match your desired indexing
                    break

        # Display interval indices in the interval_list
        for index in interval_indices:
            guiobj.interval_list.insert(tk.END, index)

        QuantizationTest2("Quan2_input.txt", interval_indices, encoded_values, quantized_values, error_list)

    else:
        QuantizationTest1("Quan1_input.txt", encoded_values, quantized_values)

def QuantizationTest2(file_name, Your_IntervalIndices, Your_EncodedValues, Your_QuantizedValues, Your_SampledError):
    expectedIntervalIndices = []
    expectedEncodedValues = []
    expectedQuantizedValues = []
    expectedSampledError = []
    with open("Quan2_Out.txt", 'r') as f:
        line = f.readline()
        line = f.readline()
        line = f.readline()
        line = f.readline()
        while line:
            # process line
            L = line.strip()
            if len(L.split(' ')) == 4:
                L = line.split(' ')
                V1 = int(L[0])
                V2 = str(L[1])
                V3 = float(L[2])
                V4 = float(L[3])
                expectedIntervalIndices.append(V1)
                expectedEncodedValues.append(V2)
                expectedQuantizedValues.append(V3)
                expectedSampledError.append(V4)
                line = f.readline()
            else:
                break
    if (len(Your_IntervalIndices) != len(expectedIntervalIndices)
            or len(Your_EncodedValues) != len(expectedEncodedValues)
            or len(Your_QuantizedValues) != len(expectedQuantizedValues)
            or len(Your_SampledError) != len(expectedSampledError)):
        print(Your_EncodedValues)
        print(expectedEncodedValues)
        print("QuantizationTest2 Test case failed, your signal have different length from the expected one")
        return
    for i in range(len(Your_IntervalIndices)):
        if (Your_IntervalIndices[i] != expectedIntervalIndices[i]):
            print("QuantizationTest2 Test case failed, your signal have different indicies from the expected one")
            return
    for i in range(len(Your_EncodedValues)):
        if (Your_EncodedValues[i] != expectedEncodedValues[i]):
            print(
                "QuantizationTest2 Test case failed, your EncodedValues have different EncodedValues from the expected one")
            return

    for i in range(len(expectedQuantizedValues)):
        if abs(Your_QuantizedValues[i] - expectedQuantizedValues[i]) < 0.01:
            continue
        else:
            print(
                "QuantizationTest2 Test case failed, your QuantizedValues have different values from the expected one")
            return
    for i in range(len(expectedSampledError)):
        if abs(Your_SampledError[i] - expectedSampledError[i]) < 0.01:
            continue
        else:
            print("QuantizationTest2 Test case failed, your SampledError have different values from the expected one")
            return
    print("QuantizationTest2 Test case passed successfully")


def QuantizationTest1(file_name,Your_EncodedValues,Your_QuantizedValues):
    expectedEncodedValues=[]
    expectedQuantizedValues=[]
    with open("Quan1_Out.txt", 'r') as f:
        line = f.readline()
        line = f.readline()
        line = f.readline()
        line = f.readline()
        while line:
            # process line
            L=line.strip()
            if len(L.split(' '))==2:
                L=line.split(' ')
                V2=str(L[0])
                V3=float(L[1])
                expectedEncodedValues.append(V2)
                expectedQuantizedValues.append(V3)
                line = f.readline()
            else:
                break
    if( (len(Your_EncodedValues)!=len(expectedEncodedValues)) or (len(Your_QuantizedValues)!=len(expectedQuantizedValues))):
        print("QuantizationTest1 Test case failed, your signal have different length from the expected one")
        return
    for i in range(len(Your_EncodedValues)):
        if(Your_EncodedValues[i]!=expectedEncodedValues[i]):
            print("QuantizationTest1 Test case failed, your EncodedValues have different EncodedValues from the expected one")
            return
    for i in range(len(expectedQuantizedValues)):
        if abs(Your_QuantizedValues[i] - expectedQuantizedValues[i]) < 0.01:
            continue
        else:
            print("QuantizationTest1 Test case failed, your QuantizedValues have different values from the expected one")
            return
    print("QuantizationTest1 Test case passed successfully")

