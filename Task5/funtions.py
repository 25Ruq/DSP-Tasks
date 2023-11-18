from Task4.transformation import modify, transform
from Task5.comparesignal2 import *

def DCT(guiobj):
    print("dummy 1")


def remove_DC(guiobj):
    transform(guiobj, 5)
    modify(guiobj.lst[0].count, 0, 0, 0, guiobj.lst[0])
    guiobj.transformation_var.set("IDFT")
    transform(guiobj, 5)
    SignalSamplesAreEqual(guiobj.outfile_name, guiobj.lst[0].samples)

