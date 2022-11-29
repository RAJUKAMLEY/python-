#TKINTER is the standard GUI libary for python . python when combined with tkinter provides a fast and easy way to creatw GUI applications Tkinter provides a powerful object-oriented infterface to the TK GUI toolkit
# TKINTER , PyQt ,wxPython for GUI PROGRAMMING
import tkinter
from tkinter import *    # * we used becz function all programs import

root=tkinter.TK()
root.title("raju")
# changing length 
root.geometry("600x600")

#LABEL
label=tkinter.Label(root , text="butterfly").pack() #
root.mainloop()

