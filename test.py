# -*- coding: utf-8 -*-
"""
Created on Mon Jun 27 11:18:19 2016

@author: anasbarakat
"""

#from tkinter import ttk
from tkinter import *
import ttk 


root = Tk()

pb = ttk.Progressbar(root, orient="horizontal", length=200, mode="determinate")
pb.pack()
pb.start()

root.mainloop()
