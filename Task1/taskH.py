from tkinter import *
import numpy as np
import matplotlib as plt
file_path = r'C:\Users\Haneen Ibrahim\Documents\GitHub\DSP-Tasks\Task1\Signals\signal1.txt'

class sig:

    def __init__(self):
        self.signal1 = None

    def read_signal(self ,file_path):

        with open(file_path, 'r') as file:
            lines = file.read().splitlines()
            # Assuming the file format as described
            count_samples = int(lines[2])
            signal_samples = [float(line.split()[1]) for line in lines[3:]]
            self.signal1 = np.array(signal_samples)
            print(f"{count_samples} samples have been successfully read and stored.")

    def display_continues_signal(self):
        if self.signal1 is not None :
            plt.title("Continues Signal")
            plt.xlabel("Time")
            plt.ylabel("Amplitude")
            plt.plot(self.signal1, label='Signal 1')
            plt.legend()
            plt.show()
        else:
            print("No signal data to display.")

    def display_discrete_signal(self):
      if self.signal1 is not None:
          plt.stem(self.signal1)
          plt.title("Discrete Signal")
          plt.xlabel("Sample")
          plt.ylabel("Amplitude")
          plt.grid()
          plt.show()
      else:
          print("No signal data to display.")

def gui():
    obj = sig()
    obj.read_signal(file_path)
    obj.display_continues_signal()
    obj.display_discrete_signal()
def main():
    root = Tk()
    root.geometry("250x170")
    Display = Button(root, height =10 ,width = 20, text ="Generate Wave",command = lambda:gui())
    Display.pack()
    mainloop()

if __name__ == "__main__":
    main()