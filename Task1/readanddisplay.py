from Task1.signal import Signal


def read_display():
    obj = Signal()
    obj.read_signal(r'Signals/signal1.txt')
    obj.plot_signals()
