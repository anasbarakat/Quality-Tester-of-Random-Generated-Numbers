# -*- coding: utf-8 -*-
"""
Created on Wed Jun 29 06:39:06 2016

@author: anasbarakat
"""

from cx_Freeze import setup, Executable

# On appelle la fonction setup
setup(
    name = "Testeur de qualité de nombres aléatoires",
    version = "1",
    description = "GUI Testeur",
    executables = [Executable("gui_test-mac.py")],
)