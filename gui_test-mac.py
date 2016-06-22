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
from PIL import Image, ImageTk


##Interface Graphique

fenetre = Tk()
fenetre.title('Sure or not Sure That is the Question?')

"""
#Ajout d'un Background
photo = PhotoImage(file="C:/Users/Azoulay/Desktop/PAF-incertitude/de.gif")
canvas = Canvas(fenetre,width=1, height=1)
canvas.pack(fill=BOTH, expand=1)
canvas.create_image(0, 0,  image=photo, anchor=NW)
#fenetre.geometry('381x350')
"""

""" Lignes de saisies  """

fenetre.geometry('800x400')

"""Ajout d'un Background
photo = PhotoImage(file="Users/anasbarakat/Documents/PAF-incertitude/de.png")
canvas = Canvas(fenetre,width=1, height=1)
canvas.pack(fill=BOTH, expand=1)
canvas.create_image(0, 0,  image=photo, anchor=NW)"""


""" Lignes de saisies  """
"""
cadre=Frame(fenetre)
cadre.pack()
Fond = Canvas(fenetre, width = 800, height = 400, bg = 'white')
Fond.pack()
"""

#insertion du titre 
photo = PhotoImage(file='/Users/anasbarakat/Documents/PAF-incertitude/titre.gif')
#canvas = Canvas(fenetre,width=10, height=10)
#canvas.pack(fill=BOTH, expand=1)
#canvas.create_image(10, 10,  image=photo, anchor=NW)
#canvas.pack()
title = Label(fenetre, image = photo)
title.pack()
title.place(x=50, y= 20)

#image de fond 
photo2 = PhotoImage(file='/Users/anasbarakat/Documents/PAF-incertitude/de.gif')
fond = Label(fenetre, image = photo2)
fond.pack()
fond.place(x=50, y= 100)

y1= 100
Label1 = Label(fenetre, text = 'Input Data File :')
Label1.pack()
Label1.place(x=85, y=y1)
File= StringVar()
Champ1 = Entry(fenetre, textvariable= File, bg ='bisque', fg='maroon')
Champ1.focus_set()
Champ1.pack()
#Champ1.place(x=175, y=25)

Champ1.place(x=200, y=y1)


y2=y1+30
Label2 = Label(fenetre, text = 'BitStream length :')
Label2.pack()
Label2.place(x=75, y=y2)
bsl= StringVar()
Champ2 = Entry(fenetre, textvariable= bsl, bg ='bisque', fg='maroon')
Champ2.focus_set()
Champ2.pack()
#Champ2.place(x=175, y=50)
Champ2.place(x=200, y=y2)


y3=y2+30
Label3 = Label(fenetre, text = 'Number of Bitestream :')
Label3.pack()
Label3.place(x=45, y=y3)
nob= StringVar()
Champ3 = Entry(fenetre, textvariable= nob, bg ='bisque', fg='maroon')
Champ3.focus_set()
Champ3.pack()
#Champ3.place(x=175, y=75)
Champ3.place(x=200, y=y3)

y4=y3+30
Label4 = Label(fenetre, text = 'Block Length (M) :')
Label4.pack()
Label4.place(x=75, y=y4)
nobl= StringVar()
Champ4 = Entry(fenetre, textvariable= nobl, bg ='bisque', fg='maroon')
Champ4.focus_set()
Champ4.pack()
#Champ4.place(x=175, y=100)
Champ4.place(x=200, y=y4)


Label5 = Label(fenetre)
Label5.pack(side = LEFT, padx = 10, pady = 10)
Label5.place(x=110,y=300)


# Radiobutton pour le choix de L'algorithme
y11=240
y12=y11+30
y13=y12+30
y14=y13+30
val = StringVar() 
bout1 = Radiobutton(fenetre, text="Frequency Test", variable=val, val=1)
bout2 = Radiobutton(fenetre, text="Frequency Test Within a Block", variable=val, val=2)
bout3 = Radiobutton(fenetre, text="Discrete Fourier Transform Test", variable=val, val=3)
bout4 = Radiobutton(fenetre, text="Linear Complexity Test", variable=val, val=4)
bout1.pack()
bout1.place(x=75,y=y11)
bout2.pack()
bout2.place(x=75,y=y12)
bout3.pack()
bout3.place(x=75,y=y13)
bout4.pack()
bout4.place(x=75,y=y14)

# Radiobutton pour le choix du graphe
y21=240
y22=y21+30
y23=y22+30
value = StringVar() 
bouton1 = Radiobutton(fenetre, text="Bar Chart", variable=value, value=1)
bouton2 = Radiobutton(fenetre, text="Pie Chart", variable=value, value=2)
bouton3 = Radiobutton(fenetre, text="Curve", variable=value, value=3)
bouton1.pack()
bouton1.place(x=300,y=y21)
bouton2.pack()
bouton2.place(x=300,y=y22)
bouton3.pack()
bouton3.place(x=300,y=y23)

cadre = Frame(fenetre, width=768, height=576, borderwidth=1)
cadre.pack(fill=BOTH)

message = Label(cadre)
message.pack(side="top", fill=X)

# barre de menu 
def alert():
    showinfo("alerte", "Bravo!")
menubar = Menu(fenetre)

menu1 = Menu(menubar, tearoff=0)
menu1.add_command(label="Créer", command=alert)
menu1.add_command(label="Editer", command=alert)
menu1.add_separator()
menu1.add_command(label="Quitter", command=fenetre.quit)
menubar.add_cascade(label="Fichier", menu=menu1)

menu2 = Menu(menubar, tearoff=0)
menu2.add_command(label="Couper", command=alert)
menu2.add_command(label="Copier", command=alert)
menu2.add_command(label="Coller", command=alert)
menubar.add_cascade(label="Editer", menu=menu2)

menu3 = Menu(menubar, tearoff=0)
menu3.add_command(label="A propos", command=alert)
menubar.add_cascade(label="Aide", menu=menu3)

fenetre.config(menu=menubar)



#Bouton pour lancer le Programme
def Lancer():
    type_graphe = int(value.get())
    algo = int(val.get())
    file = str(Champ1.get())
    BitStream_Length = int(Champ2.get())
    Nb_of_BitStream = int(Champ3.get())
    BlockLength = int(Champ4.get())

    
    if(BitStream_Length< 100 and algo==1):
        messagebox.showinfo("Input Size Recommendation","Choose a minimum of 100 bits")
        
    if(BlockLength < 20 and algo==2):
        messagebox.showinfo("Input Size Recommendation",
        "The block size should be higher than 20, please modify the parameters")
    
    if( BlockLength < 0.01*BitStream_Length and algo ==2):
        messagebox.showinfo("Input Size Recommendation",
      "Choose a minimum of 10% of the bitstream length for the number of blocks")
      
    if(BitStream_Length< 1000 and algo==3):
        messagebox.showinfo("Input Size Recommendation","Choose a minimum of 1000 bits") 
        
    if(BitStream_Length< 1000000 and algo==4):
        messagebox.showinfo("Input Size Recommendation","Choose a minimum of 10^6 bits") 
    
    if((BlockLength < 500 or BlockLength >5000 )  and algo ==2):
        messagebox.showinfo("Input Size Recommendation","The number of blocks must be between 500 and 5000")

    if(algo == 1):
        f = [frequencyTest(BitStream_Length,epsilon[i:i+BitStream_Length]) for i in range(0,BitStream_Length* Nb_of_BitStream,BitStream_Length)]
    if(algo == 2):
         f = [frequencyTestBlock(BitStream_Length, BlockLength, epsilon[i:i+BitStream_Length]) for i in range(0,BitStream_Length* Nb_of_BitStream,BitStream_Length)]
    if(algo == 3):
        f = [P_value(BitStream_Length,epsilon[i:i+BitStream_Length]) for i in range(0,BitStream_Length* Nb_of_BitStream,BitStream_Length)] 
    if(algo == 4):
        f = [linearComplexityTest(BitStream_Length, BlockLength, epsilon[i:i+BitStream_Length]) for i in range(0,BitStream_Length* Nb_of_BitStream,BitStream_Length)] 
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
bouton_lancer.place(x=150,y=350)


fenetre.mainloop()
raise Exception('exit') # pour quitter proprement 
