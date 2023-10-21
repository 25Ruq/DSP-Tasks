from tkinter import *
import numpy as np
from Signals.Sin_Cos.comparesignals import SignalSamplesAreEqual
from taskH import sig

def generate_verify():
    wave = generateWave()
    wavetype = var.get()
    if wavetype == "sin":
        SignalSamplesAreEqual(r'C:\Users\Haneen Ibrahim\Documents\GitHub\DSP-Tasks\Task1\Signals\Sin_Cos\SinOutput.txt',
                              int(sfreqText.get("1.0", "end-1c")), wave)
    elif wavetype == "cos":
        SignalSamplesAreEqual(r'C:\Users\Haneen Ibrahim\Documents\GitHub\DSP-Tasks\Task1\Signals\Sin_Cos\CosOutput.txt',
                              int(sfreqText.get("1.0", "end-1c")), wave)
def generateWave():
    amp = int(ampText.get("1.0", "end-1c"))

    theta = float(thetaText.get("1.0", "end-1c"))
    freq = int(freqText.get("1.0", "end-1c"))
    sfreq = int(sfreqText.get("1.0", "end-1c"))
    time = np.arange(0, 1, 1 / sfreq)
    wavetype = var.get()
    wave = None
    if wavetype == "sin":
        wave = amp * np.sin(2 * np.pi * freq * time + theta)
    elif wavetype == "cos":
        wave = amp * np.cos(2 * np.pi * freq * time + theta)
    obj = sig()
    obj.signal1 = wave
    obj.display_continues_signal()
    obj.display_discrete_signal()
    return wave


root = Tk()
root.geometry("350x270")

labels = ["Amplitude:", "Phase Shift ", "Analog Frequency:", "sampling Frequency:"]
for i, label_text in enumerate(labels):
    label = Label(root, text=label_text)
    label.grid(row=i, column=0, sticky="w")

ampText = Text(root, height=2, width=20)
thetaText = Text(root, height=2, width=20)
freqText = Text(root, height=2, width=20)
sfreqText = Text(root, height=2, width=20)
var = StringVar()
sinWave = Radiobutton(root, text = "sin", variable=var, value = "sin").grid(row=5, column=1)
cosWave = Radiobutton(root, text = "cos", variable=var, value = "cos").grid(row=6, column=1)

Display = Button(root, height =4 ,width = 15, text ="Generate Wave" ,command = lambda:generate_verify() ,foreground="red" ,compound="right")

ampText.grid(row=0, column=1)
thetaText.grid(row=1, column=1)
freqText.grid(row=2, column=1)
sfreqText.grid(row=3, column=1)
Display.grid(row=7, column=1)

mainloop()
