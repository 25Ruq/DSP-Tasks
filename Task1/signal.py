import math
import numpy as np
import matplotlib.pyplot as plt


class Signal:

    def __init__(self):
        self.domain = None
        self.periodicity = None
        self.count = None
        self.indices = None
        self.samples = None

    def read_signal(self, file_path, switch=0):
        with open(file_path, 'r') as file:
            lines = file.read().splitlines()
            # Assuming the file format as described
            self.domain = int(lines[0])
            self.periodicity = int(lines[1])
            self.count = int(lines[2])
            if self.domain == 0 or switch == 1:
                self.indices = np.array([float(line.split()[0]) for line in lines[3:]])
                self.samples = np.array([float(line.split()[1]) for line in lines[3:]])
            elif self.domain == 1:
                self.indices = np.array(range(0, self.count, 1))
                val = []
                for line in lines[3:]:
                    a = float(line.split()[0])
                    theta = math.radians(float(line.split()[1]))
                    x = complex(a * math.cos(theta), a * math.sin(theta))
                    val.append(x)
                self.samples = np.array(val)
            print(f"{self.count} samples have been successfully read and stored.")

    def write_signal(self, filename):
        file = open(filename, "w")
        file.write(f"{self.domain}\n")
        file.write(f"{self.periodicity}\n")
        file.write(f"{self.count}\n")
        for i in range(self.count):
            file.write(f"{self.indices[i]} {self.samples[i]}\n")
        file.close()

    def store_signal(self, domain, periodicity, count, indices, samples):
        self.domain = domain
        self.periodicity = periodicity
        self.count = count
        self.samples = samples
        self.indices = indices

    def display_signal(self):
        print(self.domain, '\n')
        print(self.periodicity, '\n')
        print(self.count, '\n')
        print(self.indices, '\n')
        print(self.samples, '\n')

    def plot_signals(self, ff_list=[]):
        if self.domain == 0:
            plt.figure(figsize=(10, 6))
            # Plot the analog (continuous) signal
            plt.subplot(2, 1, 1)
            plt.plot(self.indices, self.samples)
            plt.title("Time Domain Analog Signal")
            plt.xlabel("Time")
            plt.ylabel("Amplitude")
            plt.grid(True)
            # Plot the digital (discrete) signal
            plt.subplot(2, 1, 2)
            plt.stem(self.indices, self.samples, basefmt=' ')
            plt.title("Time Domain Digital Signal")
            plt.xlabel("Sample")
            plt.ylabel("Amplitude")
            plt.grid(True)
            plt.tight_layout()
            plt.show()
        elif self.domain == 1 and ff_list:
            plt.figure(figsize=(10, 6))
            # Plot the amplitude against frequency
            plt.subplot(2, 1, 1)
            plt.bar(ff_list, self.indices)
            plt.title("Frequency Domain Digital Signal")
            plt.xlabel("Frequency")
            plt.ylabel("Amplitude")
            plt.grid(True)
            # Plot the phase shift against frequency
            plt.subplot(2, 1, 2)
            plt.bar(ff_list, self.samples)
            plt.title("Frequency Domain Digital Signal")
            plt.xlabel("Frequency")
            plt.ylabel("Phase Shift")
            plt.grid(True)
            plt.tight_layout()
            plt.show()
