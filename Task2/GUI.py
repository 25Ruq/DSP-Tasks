from tkinter import *
from task2R import shift, norm, accumulate


root = Tk()
canvas = Canvas(root, width=400, height=300)
canvas.pack()
signals = [
    "Signal1",
    "Signal2",
    "signal3"
]

# 5
shiftVal = Text(root, height=2, width=15)
canvas.create_window(75, 100, window=shiftVal)
shiftButton = Button(root, text="Shift", command=lambda: shift(shiftVal))
shiftButton.config(width=10)
canvas.create_window(200, 100, window=shiftButton)

# 6
ranges = [
    "[0,1]",
    "[-1,1]"
]
selectedSignal_n = StringVar()
selectedSignal_n.set("Select Signal")
selectedRange = StringVar()
selectedRange.set("Select Range")
SignalMenu_n = OptionMenu(root, selectedSignal_n, *signals)
SignalMenu_n.config(width=10)
canvas.create_window(75, 150, window=SignalMenu_n)
rangeMenu = OptionMenu(root, selectedRange, *ranges)
rangeMenu.config(width=15)
canvas.create_window(200, 150, window=rangeMenu)
normButton = Button(root, text="Normalize", command=lambda: norm(selectedSignal_n,selectedRange))
normButton.config(width=10)
canvas.create_window(325, 150, window=normButton)

# 7
selectedSignal_ac = StringVar()
selectedSignal_ac.set("Select Signal")
SignalMenu_ac = OptionMenu(root, selectedSignal_ac, *signals)
SignalMenu_ac.config(width=10)
canvas.create_window(75, 200, window=SignalMenu_ac)
accumulateButton = Button(root, text="Accumulate", command=lambda: accumulate(selectedSignal_ac))
accumulateButton.config(width=10)
canvas.create_window(200, 200, window=accumulateButton)

mainloop()
