#!/usr/bin/env python
#-*- coding: utf-8 -*-

from math import *
import matplotlib.pyplot as plt
import numpy as np
import scipy as sp
from scipy import special
from itertools import groupby
from tkinter import *
from tkinter.messagebox import *


fenetre = Tk()
fenetre.title('Sure or not Sure That is the Question?')

"""Lignes de saisies"""

Label1 = Label(fenetre, text = 'Input Data File :')
Label1.pack(side = LEFT, padx=5, pady=5)
File= StringVar()
Champ1 = Entry(fenetre, textvariable= File, bg ='bisque', fg='maroon')
Champ1.focus_set(side=LEFT, padx=5, pady=5)
Champ1.pack()


Label2 = Label(fenetre, text = 'BitStream length :')
Label2.pack(side=BOTTOM, padx=5, pady=5)
bsl= StringVar()
Champ2 = Entry(fenetre, textvariable= bsl, bg ='bisque', fg='maroon')
Champ2.focus_set()
Champ2.pack(side=BOTTOM, padx=5, pady=5)
"""

Label3 = Label(fenetre, text = 'Number of Bitestream :')
Label3.pack()
nob= StringVar()
Champ3 = Entry(fenetre, textvariable= nob, bg ='bisque', fg='maroon')
Champ3.focus_set()
Champ3.pack()


Label4 = Label(fenetre, text = 'Number of Block :')
Label4.pack()
nobl= StringVar()
Champ4 = Entry(fenetre, textvariable= nobl, bg ='bisque', fg='maroon')
Champ4.focus_set()
Champ4.pack()

# Radiobutton pour le choix du graphe
value = StringVar() 
bouton1 = Radiobutton(fenetre, text="Histogramme", variable=value, value=1)
bouton2 = Radiobutton(fenetre, text="Camembert", variable=value, value=2)
bouton3 = Radiobutton(fenetre, text="Courbe", variable=value, value=3)
bouton1.pack()
bouton2.pack()
bouton3.pack()



#Bouton pour lancer le Programme
bouton_lancer = Button(text='Lancer', command=Executer)
bouton_lancer.pack()

"""


fenetre.mainloop()
 
 
def Executer():
    a = float(e1.get())
    b = float(e2.get())
    c = float(e3.get())
    result = a+(a*b/c)/100
    lbl1.config(text = 'result '+str(result))
 
root = Tk()
e1 = Entry()
e2 = Entry()
e3 = Entry()
e1.pack()
e2.pack()
e3.pack()

lbl1 = Label()
lbl1.pack()
 