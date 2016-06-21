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
from pyzpaf import *


##Interface Graphique

fenetre = Tk()
fenetre.title('Sure or not Sure That is the Question?')

#Ajout d'un Background
photo = PhotoImage(file="C:/Users/Azoulay/Desktop/PAF-incertitude/de.gif")
canvas = Canvas(fenetre,width=1, height=1)
canvas.pack(fill=BOTH, expand=1)
canvas.create_image(0, 0,  image=photo, anchor=NW)
fenetre.geometry('381x307')


""" Lignes de saisies  """

Label1 = Label(fenetre, text = 'Input Data File :')
Label1.pack(side = LEFT, padx = 10, pady = 10)
File= StringVar()
Champ1 = Entry(fenetre, textvariable= File, bg ='bisque', fg='maroon')
Champ1.focus_set()
Champ1.pack(side = LEFT, padx = 10, pady = 10)


Label2 = Label(fenetre, text = 'BitStream length :')
Label2.pack( side = LEFT,padx = 10, pady = 10)
bsl= StringVar()
Champ2 = Entry(fenetre, textvariable= bsl, bg ='bisque', fg='maroon')
Champ2.focus_set()
Champ2.pack( side = LEFT,padx = 10, pady = 10)


Label3 = Label(fenetre, text = 'Number of Bitestream :')
Label3.pack(side = LEFT, padx = 10, pady = 10)
nob= StringVar()
Champ3 = Entry(fenetre, textvariable= nob, bg ='bisque', fg='maroon')
Champ3.focus_set()
Champ3.pack(side = LEFT, padx = 10, pady = 10)


Label4 = Label(fenetre, text = 'Number of Block :')
Label4.pack(side = LEFT, padx = 10, pady = 10)
nobl= StringVar()
Champ4 = Entry(fenetre, textvariable= nobl, bg ='bisque', fg='maroon')
Champ4.focus_set()
Champ4.pack(side = LEFT, padx = 10, pady = 10)


Label5 = Label(fenetre)
Label5.pack(side = BOTTOM, padx = 10, pady = 10)

# Radiobutton pour le choix de L'algorithme
val = StringVar() 
bout1 = Radiobutton(fenetre, text="Algorithme 1", variable=val, val=1)
bout2 = Radiobutton(fenetre, text="Algorithme 2", variable=val, val=2)
bout3 = Radiobutton(fenetre, text="Algorithme 6", variable=val, val=3)
bout4 = Radiobutton(fenetre, text="Algorithme 10", variable=val, val=4)
bout1.pack()
bout2.pack()
bout3.pack()
bout4.pack()

# Radiobutton pour le choix du graphe
value = StringVar() 
bouton1 = Radiobutton(fenetre, text="Histogramme", variable=value, value=1)
bouton2 = Radiobutton(fenetre, text="Camembert", variable=value, value=2)
bouton3 = Radiobutton(fenetre, text="Courbe", variable=value, value=3)
bouton1.pack()
bouton2.pack()
bouton3.pack()


#Bouton pour lancer le Programme
def Lancer():
    type_graphe = int(value.get())
    algo = int(val.get())
    file = str(Champ1.get())
    BitStream_Length = int(Champ2.get())
    
    
    Label5.config(text = 'Result : ' + pourcentage + ' %')    

bouton_lancer = Button(fenetre, text='Lancer', command=Lancer)
bouton_lancer.pack(side = BOTTOM, padx = 5, pady = 5)
 
"""
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
"""

fenetre.mainloop()