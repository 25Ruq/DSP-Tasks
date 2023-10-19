from tkinter import *
import numpy as np
from Signals.Sin_Cos.comparesignals import SignalSamplesAreEqual
from taskH import sig

def generate_verify():
    wave = generateWave()
    wavetype = var.get()
    if wavetype == "sin":
        SignalSamplesAreEqual(r'C:\Users\hb\PycharmProjects\DSP_Task1\Signals\Sin_Cos\SinOutput.txt',
                              int(sfreqText.get("1.0", "end-1c")), wave)
    elif wavetype == "cos":
        SignalSamplesAreEqual(r'C:\Users\hb\PycharmProjects\DSP_Task1\Signals\Sin_Cos\CosOutput.txt',
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
root.geometry("250x170")
ampText = Text(root, height=5, width=25)
thetaText = Text(root, height=5, width=25)
freqText = Text(root, height=5, width=25)
sfreqText = Text(root, height=5, width=25)
var = StringVar()
sinWave = Radiobutton(root, text = "sin", variable=var, value = "sin").pack(side = TOP, ipady = 5)
cosWave = Radiobutton(root, text = "cos", variable=var, value = "cos").pack(side = TOP, ipady = 5)

Display = Button(root, height =10 ,width = 20, text ="Generate Wave",command = lambda:generate_verify())

ampText.pack()
thetaText.pack()
freqText.pack()
sfreqText.pack()
Display.pack()

mainloop()
