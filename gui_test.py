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
fenetre.geometry('381x350')


"""Ajout d'un Background
photo = PhotoImage(file="Users/anasbarakat/Documents/PAF-incertitudeRepo/de.gif")
canvas = Canvas(fenetre,width=1, height=1)
canvas.pack(fill=BOTH, expand=1)
canvas.create_image(0, 0,  image=photo, anchor=NW)
"""



""" Lignes de saisies  """

Label1 = Label(fenetre, text = 'Input Data File :')

Label1.pack()
Label1.place(x=85, y=25)
File= StringVar()
Champ1 = Entry(fenetre, textvariable= File, bg ='bisque', fg='maroon')
Champ1.focus_set()
Champ1.pack()
Champ1.place(x=175, y=25)


Label2 = Label(fenetre, text = 'BitStream length :')
Label2.pack()
Label2.place(x=75, y=50)

bsl= StringVar()
Champ2 = Entry(fenetre, textvariable= bsl, bg ='bisque', fg='maroon')
Champ2.focus_set()
Champ2.pack()
Champ2.place(x=175, y=50)

Label3 = Label(fenetre, text = 'Number of Bitestream :')
Label3.pack()
Label3.place(x=45, y=75)
nob= StringVar()
Champ3 = Entry(fenetre, textvariable= nob, bg ='bisque', fg='maroon')
Champ3.focus_set()
Champ3.pack()
Champ3.place(x=175, y=75)

Label4 = Label(fenetre, text = 'Number of Block :')
Label4.pack()
Label4.place(x=75, y=100)
nobl= StringVar()
Champ4 = Entry(fenetre, textvariable= nobl, bg ='bisque', fg='maroon')
Champ4.focus_set()
Champ4.pack()
Champ4.place(x=175, y=100)


Label5 = Label(fenetre)
Label5.pack(side = LEFT, padx = 10, pady = 10)
Label5.place(x=110,y=300)

# Radiobutton pour le choix de L'algorithme
val = StringVar() 
bout1 = Radiobutton(fenetre, text="Algorithme 1", variable=val, val=1)
bout2 = Radiobutton(fenetre, text="Algorithme 2", variable=val, val=2)
bout3 = Radiobutton(fenetre, text="Algorithme 6", variable=val, val=3)
bout4 = Radiobutton(fenetre, text="Algorithme 10", variable=val, val=4)
bout1.pack()
bout1.place(x=20,y=130)
bout2.pack()
bout2.place(x=20,y=160)
bout3.pack()
bout3.place(x=20,y=190)
bout4.pack()
bout4.place(x=20,y=220)

# Radiobutton pour le choix du graphe
value = StringVar() 
bouton1 = Radiobutton(fenetre, text="Histogramme", variable=value, value=1)
bouton2 = Radiobutton(fenetre, text="Camembert", variable=value, value=2)
bouton3 = Radiobutton(fenetre, text="Courbe", variable=value, value=3)
bouton1.pack()
bouton1.place(x=220,y=130)
bouton2.pack()
bouton2.place(x=220,y=160)
bouton3.pack()
bouton3.place(x=220,y=190)

cadre = Frame(fenetre, width=768, height=576, borderwidth=1)
cadre.pack(fill=BOTH)

message = Label(cadre, text="Notre fenêtre")
message.pack(side="top", fill=X)

#organisation en frames 
fenetre['bg']='white'

# frame 1
Frame1 = Frame(fenetre, borderwidth=2, relief=GROOVE)
Frame1.pack(side=LEFT, padx=30, pady=30)

# frame 2
Frame2 = Frame(fenetre, borderwidth=2, relief=GROOVE)
Frame2.pack(side=LEFT, padx=10, pady=10)

# frame 3 dans frame 2
Frame3 = Frame(Frame2, bg="white", borderwidth=2, relief=GROOVE)
Frame3.pack(side=RIGHT, padx=5, pady=5)

# Ajout de labels
Label(Frame1, text="Frame 1").pack(padx=10, pady=10)
Label(Frame2, text="Frame 2").pack(padx=10, pady=10)
Label(Frame3, text="Frame 3",bg="white").pack(padx=10, pady=10)



#Bouton pour lancer le Programme
def Lancer():
    type_graphe = int(value.get())
    algo = int(val.get())
    file = str(Champ1.get())
    BitStream_Length = int(Champ2.get())
    Nb_of_BitStream = int(Champ3.get())
    Nb_of_Block = int(Champ2.get())
    if(algo == 1):
        f = [frequencyTest(BitStream_Length,epsilon[i:i+BitStream_Length]) for i in range(0,BitStream_Length* Nb_of_BitStream,BitStream_Length)]
    if(algo == 2):
         f = [frequencyTestBlock(BitStream_Length, Nb_of_Block, epsilon[i:i+BitStream_Length]) for i in range(0,BitStream_Length* Nb_of_BitStream,BitStream_Length)]
    if(algo == 3):
        f = [P_value(BitStream_Length,epsilon[i:i+BitStream_Length]) for i in range(0,BitStream_Length* Nb_of_BitStream,BitStream_Length)] 
    if(algo == 4):
        f = [linearComplexityTest(BitStream_Length,Nb_of_Block, epsilon[i:i+BitStream_Length]) for i in range(0,BitStream_Length* Nb_of_BitStream,BitStream_Length)] 
    if(type_graphe == 1):
        hist(f)
    if(type_graphe == 2):
        circ(f)
    if(type_graphe == 3):
        curve(f)
    p = percent(f)*100
    Label5.config(text = 'Result : Proportion = ' + str(p)  + ' %')    


bouton_lancer = Button(fenetre, text='Lancer', command=Lancer)
bouton_lancer.pack(side = BOTTOM, padx = 5, pady = 5)
bouton_lancer.place(x=250,y=250)

fenetre.mainloop()