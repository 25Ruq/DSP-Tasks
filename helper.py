import os
from tkinter import filedialog, END
from Task1.signal import Signal


def open_task(root,task, directory):
    try:
        os.chdir(directory)
        root.destroy()
        task()
    except FileNotFoundError:
        root.destroy()
        task()


def select_signal(guiobj):
    file_path = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt")])
    if file_path:
        obj = Signal()
        obj.read_signal(file_path)
        obj.plot_signals()
        guiobj.lst.append(obj)
        guiobj.signals_listbox.insert(END, os.path.basename(file_path))


def remove_signal(guiobj):
    try:
        selected_item_index = guiobj.signals_listbox.curselection()
        guiobj.lst.pop(int(selected_item_index[0]))
    except IndexError:
        return
    if selected_item_index:
        guiobj.signals_listbox.delete(selected_item_index)
