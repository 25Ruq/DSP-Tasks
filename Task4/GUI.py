from tkinter import *
from Task4.transformation import transform
from helper import select_signal, remove_signal


class Transformation:
    def __init__(self):
        self.lst = []
        self.root = Tk()
        self.root.geometry("350x350")

        self.current_label = Label(self.root, text="Current Signal:")
        self.signals_listbox = Listbox(self.root, width=27, height=2)
        self.current_label.grid(row=0, column=0)
        self.signals_listbox.grid(row=0, column=1)

        self.outfile_label = Label(self.root, text="Output File:")
        self.outfile_text = Text(self.root, height=2, width=20)
        self.outfile_label.grid(row=1, column=0)
        self.outfile_text.grid(row=1, column=1)

        self.select_button = Button(self.root, text="Select Signal", command=lambda: select_signal(self))
        self.select_button.config(width=20)
        self.remove_button = Button(self.root, text="Remove Signal", command=lambda: remove_signal(self))
        self.remove_button.config(width=20)
        self.select_button.grid(row=2, column=0)
        self.remove_button.grid(row=2, column=1)

        self.transformation_var = StringVar(self.root)
        self.dft = Radiobutton(self.root, text="DFT", variable=self.transformation_var, value="DFT")
        self.idft = Radiobutton(self.root, text="IDFT", variable=self.transformation_var, value="IDFT")
        self.dft.grid(row=3, column=0)
        self.idft.grid(row=3, column=1)

        self.sampling_freq_label = Label(self.root, text="Sampling Frequency:")
        self.sampling_freq_text = Text(self.root, height=2, width=20)
        self.sampling_freq_label.grid(row=4, column=0)
        self.sampling_freq_text.grid(row=4, column=1)

        self.optional_label = Label(self.root, text="Optional Input:")
        self.optional_label.grid(row=5, column=0)
        labels = ["Index:", "Amplitude:", "phase shift:"]
        for i, label_text in enumerate(labels):
            label = Label(self.root, text=label_text)
            label.grid(row=i + 6, column=0)
        self.indexText = Text(self.root, height=2, width=20)
        self.ampText = Text(self.root, height=2, width=20)
        self.thetaText = Text(self.root, height=2, width=20)
        self.indexText.grid(row=6, column=1)
        self.ampText.grid(row=7, column=1)
        self.thetaText.grid(row=8, column=1)

        self.transform_button = Button(self.root, text="Transform Signal", command=lambda: transform(self))
        self.transform_button.config(width=20)
        self.transform_button.grid(row=9, column=1)

        mainloop()
