from tkinter import *
from task2R import shift, norm, accumulate
# dummy functions that will be imported later


def arth():
    # based on op + or -
    print("dummy arth")


def multiply():
    print("dummy multiply")


def square():
    print("dummy square")


root = Tk()
canvas = Canvas(root, width=500, height=350)
canvas.pack()
signals = [
    "Signal1",
    "Signal2",
    "signal3"
]

# 1 & 2
op = [
    "+",
    "-",
]
selectedSignal_f = StringVar()
selectedSignal_f.set("Select Signal")
selectedOp = StringVar()
selectedOp.set("Select Operation")
selectedSignal_s = StringVar()
selectedSignal_s.set("Select Signal")
firstSignalMenu = OptionMenu(root, selectedSignal_f, *signals)
firstSignalMenu.config(width=10)
canvas.create_window(75, 50, window=firstSignalMenu)
opMenu = OptionMenu(root, selectedOp, *op)
opMenu.config(width=15)
canvas.create_window(200, 50, window=opMenu)
secondSignalMenu = OptionMenu(root, selectedSignal_s, *signals)
secondSignalMenu.config(width=10)
canvas.create_window(325, 50, window=secondSignalMenu)
arthButton = Button(root, text="Calculate", command=lambda: arth())
arthButton.config(width=10)
canvas.create_window(425, 50, window=arthButton)

# 3
selectedSignal_m = StringVar()
selectedSignal_m.set("Select Signal")
SignalMenu_m = OptionMenu(root, selectedSignal_m, *signals)
SignalMenu_m.config(width=10)
canvas.create_window(75, 100, window=SignalMenu_m)
scale = Text(root, height=2, width=15)
canvas.create_window(200, 100, window=scale)
multiplyButton = Button(root, text="Multiply", command=lambda: multiply())
multiplyButton.config(width=10)
canvas.create_window(325, 100, window=multiplyButton)

# 4
selectedSignal_sq = StringVar()
selectedSignal_sq.set("Select Signal")
SignalMenu_sq = OptionMenu(root, selectedSignal_sq, *signals)
SignalMenu_sq.config(width=10)
canvas.create_window(75, 150, window=SignalMenu_sq)
squareButton = Button(root, text="Square", command=lambda: square())
squareButton.config(width=10)
canvas.create_window(200, 150, window=squareButton)

# 5
shiftVal = Text(root, height=2, width=15)
canvas.create_window(75, 200, window=shiftVal)
shiftButton = Button(root, text="Shift", command=lambda: shift(shiftVal))
shiftButton.config(width=10)
canvas.create_window(200, 200, window=shiftButton)

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
canvas.create_window(75, 250, window=SignalMenu_n)
rangeMenu = OptionMenu(root, selectedRange, *ranges)
rangeMenu.config(width=15)
canvas.create_window(200, 250, window=rangeMenu)
normButton = Button(root, text="Normalize", command=lambda: norm(selectedSignal_n,selectedRange))
normButton.config(width=10)
canvas.create_window(325, 250, window=normButton)

# 7
selectedSignal_ac = StringVar()
selectedSignal_ac.set("Select Signal")
SignalMenu_ac = OptionMenu(root, selectedSignal_ac, *signals)
SignalMenu_ac.config(width=10)
canvas.create_window(75, 300, window=SignalMenu_ac)
accumulateButton = Button(root, text="Accumulate", command=lambda: accumulate(selectedSignal_ac))
accumulateButton.config(width=10)
canvas.create_window(200, 300, window=accumulateButton)

mainloop()
