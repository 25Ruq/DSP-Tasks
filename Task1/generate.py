import numpy as np
from Task1.Signals.Sin_Cos.comparesignals import SignalSamplesAreEqual
from Task1.signal import Signal


def generate_verify(guiobj):
    wave = generateWave(guiobj)
    wavetype = guiobj.var.get()
    if wavetype == "sin":
        SignalSamplesAreEqual(r'Sin_Cos\SinOutput.txt', int(guiobj.sfreqText.get("1.0", "end-1c")), wave)
    elif wavetype == "cos":
        SignalSamplesAreEqual(r'Sin_Cos\CosOutput.txt', int(guiobj.sfreqText.get("1.0", "end-1c")), wave)


def generateWave(guiobj):
    amp = int(guiobj.ampText.get("1.0", "end-1c"))
    theta = float(guiobj.thetaText.get("1.0", "end-1c"))
    freq = int(guiobj.freqText.get("1.0", "end-1c"))
    sfreq = int(guiobj.sfreqText.get("1.0", "end-1c"))
    time = np.arange(0, 1, 1 / sfreq)
    wavetype = guiobj.var.get()
    wave = None
    if wavetype == "sin":
        wave = amp * np.sin(2 * np.pi * freq * time + theta)
    elif wavetype == "cos":
        wave = amp * np.cos(2 * np.pi * freq * time + theta)
    obj = Signal()
    obj.indices = np.arange(0, sfreq, 1)
    obj.samples = wave
    obj.plot_signals()
    return wave
