from tkinter import *
from Task1.generate import generate_verify


class GenerateGUI:
    def __init__(self):
        root = Tk()
        root.geometry("350x270")
        labels = ["Amplitude:", "Phase Shift ", "Analog Frequency:", "sampling Frequency:"]
        for i, label_text in enumerate(labels):
            label = Label(root, text=label_text)
            label.grid(row=i, column=0, sticky="w")
        self.ampText = Text(root, height=2, width=20)
        self.thetaText = Text(root, height=2, width=20)
        self.freqText = Text(root, height=2, width=20)
        self.sfreqText = Text(root, height=2, width=20)
        self.var = StringVar(root)
        self.sinWave = Radiobutton(root, text="sin", variable=self.var, value="sin")
        self.cosWave = Radiobutton(root, text="cos", variable=self.var, value="cos")
        display = Button(root, height=4, width=15, text="Generate Wave", command=lambda: generate_verify(self),
                         foreground="red", compound="right")
        self.sinWave.grid(row=5, column=1)
        self.cosWave.grid(row=6, column=1)
        self.ampText.grid(row=0, column=1)
        self.thetaText.grid(row=1, column=1)
        self.freqText.grid(row=2, column=1)
        self.sfreqText.grid(row=3, column=1)
        display.grid(row=7, column=1)
        mainloop()
