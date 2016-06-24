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
fenetre.geometry('900x700')

"""Ajout d'un Background
photo = PhotoImage(file="Users/anasbarakat/Documents/PAF-incertitude/de.png")
canvas = Canvas(fenetre,width=1, height=1)
canvas.pack(fill=BOTH, expand=1)
canvas.create_image(0, 0,  image=photo, anchor=NW)"""

#insertion du titre 
photo = PhotoImage(file='/Users/anasbarakat/Documents/PAF-incertitude/titlev3.gif')
title = Label(fenetre, image = photo)
title.pack()
title.place(x=50, y= 50)

#image de fond 
photo2 = PhotoImage(file='/Users/anasbarakat/Documents/PAF-incertitude/de.gif')
fond = Label(fenetre, image = photo2)
photo2.zoom(10,10)
fond.pack()
fond.place(x=470, y= 160)

#input (bitstream and numeric parameters) 
y1= 150
Label1 = Label(fenetre, text = 'Input Data File :')
Label1.pack()
Label1.place(x=140, y=y1)


Xchamps=250
var = StringVar(fenetre)
var.set("file")
option = OptionMenu(fenetre, var, "data", "matlab")
option.pack()
option.place(x=Xchamps,y=y1)
file = var.get()


y2=y1+30
Label2 = Label(fenetre, text = 'BitStream length :')
Label2.pack()
Label2.place(x=75, y=y2)
bsl= StringVar()
Champ2 = Entry(fenetre, textvariable= bsl, bg ='bisque', fg='maroon')
Champ2.focus_set()
Champ2.pack()
#Champ2.place(x=175, y=50)
Champ2.place(x=Xchamps, y=y2)


y3=y2+30
Label3 = Label(fenetre, text = 'Number of Bitestream :')
Label3.pack()
Label3.place(x=45, y=y3)
nob= StringVar()
Champ3 = Entry(fenetre, textvariable= nob, bg ='bisque', fg='maroon')
Champ3.focus_set()
Champ3.pack()
#Champ3.place(x=175, y=75)
Champ3.place(x=Xchamps, y=y3)

y4=y3+30
Label4 = Label(fenetre, text = 'Block Length (M) :')
Label4.pack()
Label4.place(x=75, y=y4)
nobl= StringVar()
Champ4 = Entry(fenetre, textvariable= nobl, bg ='bisque', fg='maroon')
Champ4.focus_set()
Champ4.pack()
#Champ4.place(x=175, y=100)
Champ4.place(x=Xchamps, y=y4)

y5=y4+30
Label6 = Label(fenetre, text = 'Template Choice (Algo 7 et 8) :')
Label6.pack()
Label6.place(x=30, y=y5)
tc= StringVar()
Champ6 = Entry(fenetre, textvariable= tc, bg ='bisque', fg='maroon')
Champ6.focus_set()
Champ6.pack()
#Champ4.place(x=175, y=100)
Champ6.place(x=Xchamps, y=y5)

Label5 = Label(fenetre)
Label5.pack(side = LEFT, padx = 10, pady = 10)
Label5.place(x=110,y=300)


#Choix de L'algorithme
y11=350
y12=y11+30
y13=y12+30
y14=y13+30
y15=y14+30
y16=y15+30
y17=y16+30
val = StringVar() 
bout1 = Radiobutton(fenetre, text="Frequency Test (1)", variable=val, val=1)
bout2 = Radiobutton(fenetre, text="Frequency Test Within a Block (2)", variable=val, val=2)
bout3 = Radiobutton(fenetre, text="Discrete Fourier Transform Test (6)", variable=val, val=3)
bout4 = Radiobutton(fenetre, text="Linear Complexity Test (10)", variable=val, val=4)
bout5 = Radiobutton(fenetre, text="Non-overlapping Template Matching Test (7)", variable=val, val=5)
bout6 = Radiobutton(fenetre, text="Overlapping Template Matching Test (8)", variable=val, val=6)
bout7 = Radiobutton(fenetre, text="Binary Matrix Rank Test (5)", variable=val, val=7)
bout1.pack()
bout1.place(x=75,y=y11)
bout2.pack()
bout2.place(x=75,y=y12)
bout3.pack()
bout3.place(x=75,y=y13)
bout4.pack()
bout4.place(x=75,y=y14)
bout5.pack()
bout5.place(x=75,y=y15)
bout6.pack()
bout6.place(x=75,y=y16)
bout7.pack()
bout7.place(x=75,y=y17)

#Choix de la représentation graphique
y21=410
y22=y21+30
y23=y22+30
value = StringVar() 
bouton1 = Radiobutton(fenetre, text="Bar Chart", variable=value, value=1)
bouton2 = Radiobutton(fenetre, text="Pie Chart", variable=value, value=2)
bouton3 = Radiobutton(fenetre, text="Curve", variable=value, value=3)
bouton1.pack()
bouton1.place(x=400,y=y21)
bouton2.pack()
bouton2.place(x=400,y=y22)
bouton3.pack()
bouton3.place(x=400,y=y23)

#cadre = Frame(fenetre, width=768, height=576, borderwidth=1)
#cadre.pack(fill=BOTH)

#message = Label(cadre)
#message.pack(side="top", fill=X)

#Bouton pour lancer le Programme
def Lancer():
    type_graphe = int(value.get())
    algo = int(val.get())
    file = str(Champ1.get())
    # fichier = open("C:/Users/Azoulay/Desktop/PAF-incertitude/"+file+".txt", "r")
    #epsilon = fichier.read()[3:]
    #fichier.close()
    BitStream_Length = int(Champ2.get())
    Nb_of_BitStream = int(Champ3.get())
    BlockLength = int(Champ4.get())
    Template = str(Champ6.get())
    
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
    
    if((BlockLength < n/100)  and algo == 5):
        messagebox.showinfo("Input Size Recommendation","Make sure that M > n*0.01")
    
    if((BitStream_Length < 1000000)  and algo == 6):
        messagebox.showinfo("Input Size Recommendation","Choose a minimum of 10^6 bits")
        
    if(algo == 1):
        f = [frequencyTest(BitStream_Length,epsilon[i:i+BitStream_Length]) for i in range(0,BitStream_Length* Nb_of_BitStream,BitStream_Length)]
    if(algo == 2):
         f = [frequencyTestBlock(BitStream_Length, BlockLength, epsilon[i:i+BitStream_Length]) for i in range(0,BitStream_Length* Nb_of_BitStream,BitStream_Length)]
    if(algo == 3):
        f = [P_value(BitStream_Length,epsilon[i:i+BitStream_Length]) for i in range(0,BitStream_Length* Nb_of_BitStream,BitStream_Length)] 
    if(algo == 4):
        f = [linearComplexityTest(BitStream_Length, BlockLength, epsilon[i:i+BitStream_Length]) for i in range(0,BitStream_Length* Nb_of_BitStream,BitStream_Length)] 
    if(algo == 5):
        f = [NonOverlappingTemplateMatching(BitStream_Length, BlockLength, Template,  epsilon[i:i+BitStream_Length]) for i in range(0,BitStream_Length* Nb_of_BitStream,BitStream_Length)] 
    if(algo == 6):
        f = [OverlappingTemplateMatching(BitStream_Length, Template, epsilon[i:i+BitStream_Length]) for i in range(0,BitStream_Length* Nb_of_BitStream,BitStream_Length)] 
    if(algo == 7):
        f = [binaryMatrixTest(BitStream_Length,epsilon[i:i+BitStream_Length],M,Q) for i in range(0,BitStream_Length* Nb_of_BitStream,BitStream_Length)]
        
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
bouton_lancer.place(x=250,y=600)


fenetre.mainloop()
raise Exception('exit') # pour quitter proprement 
