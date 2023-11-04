import os
from tkinter import filedialog, END
from Task1.signal import Signal


def open_task(root, task, directory):
    try:
        os.chdir(directory)
        root.destroy()
        task()
    except FileNotFoundError:
        root.destroy()
        task()


def select_signal(guiobj, num=0):
    file_path = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt")])
    if file_path:
        if num == 0:
            obj = Signal()
            obj.read_signal(file_path)
            obj.plot_signals()
            guiobj.lst.append(obj)
            guiobj.signals_listbox.insert(END, os.path.basename(file_path))
        else:
            obj = Signal()
            obj.read_signal(file_path, 1)
            obj.plot_signals()
            guiobj.expected_signal = obj
            guiobj.expected_signals_listbox.delete(0, END)
            guiobj.expected_signals_listbox.insert(END, os.path.basename(file_path))


def remove_signal(guiobj, num=0):
    if num == 0:
        try:
            selected_item_index = guiobj.signals_listbox.curselection()
            guiobj.lst.pop(int(selected_item_index[0]))
        except IndexError:
            return
        if selected_item_index:
            guiobj.signals_listbox.delete(selected_item_index)
    else:
        selected_item_index = guiobj.expected_signals_listbox.curselection()
        guiobj.expected_signal = None
        if selected_item_index:
            guiobj.expected_signals_listbox.delete(selected_item_index)
