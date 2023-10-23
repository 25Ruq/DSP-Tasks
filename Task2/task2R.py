from Task1.taskH import *

def shift(shiftVal):
    obj = sig()
    obj.read_signal(r'C:\Users\hb\PycharmProjects\DSP-Tasks\Task2\Task 2 + Files\input signals\input shifting.txt')
    obj.display_continues_signal()
    obj.display_discrete_signal()
    print(obj.indices)
    obj.indices = obj.indices - int(shiftVal.get("1.0", "end-1c"))
    print(obj.indices)
    obj.display_continues_signal()
    obj.display_discrete_signal()


def norm(selectedSignal_n,selectedRange):
    path = r'C:\Users\hb\PycharmProjects\tempTasks\Task 2 + Files\input signals\\'
    path += selectedSignal_n.get() + '.txt'
    new_min = None
    new_max = None
    if selectedRange.get() == "[0,1]":
        new_min = 0
        new_max = 1
    elif selectedRange.get() == "[-1,1]":
        new_min = -1
        new_max = 1
    obj = sig()
    obj.read_signal(path)
    obj.display_continues_signal()
    obj.display_discrete_signal()
    old_min = min(obj.signal1)
    old_max = max(obj.signal1)
    obj.signal1 = ((obj.signal1-old_min)/(old_max-old_min))*(new_max-new_min)+new_min
    obj.display_continues_signal()
    obj.display_discrete_signal()


def accumulate(selectedSignal_ac):
    path = r'C:\Users\hb\PycharmProjects\tempTasks\Task 2 + Files\input signals\\'
    path += selectedSignal_ac.get() + '.txt'
    obj = sig()
    obj.read_signal(r'C:\Users\hb\PycharmProjects\tempTasks\Task 2 + Files\input signals\Signal1.txt')
    obj.display_continues_signal()
    obj.display_discrete_signal()
    for i in range(1, len(obj.signal1)):
        obj.signal1[i] = obj.signal1[i] + obj.signal1[i-1]
    obj.display_continues_signal()
    obj.display_discrete_signal()
