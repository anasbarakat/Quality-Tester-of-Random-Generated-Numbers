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

fichier = open("C:/Users/Azoulay/Downloads/paf.txt", "r")
epsilon = fichier.read()[3:]
fichier.close()

#n = int(input("Entrée la longueur n : "))

## Implémentations de Algorithmes

"""    Algorithme 1  """
def algo1(n, e):
    S_n = 0
    for i in range(n):
        S_n += 2*int(e[i])-1
    s_obs = abs(S_n)/sqrt(n)
    P_value = erfc(s_obs/sqrt(2))
    return P_value

""" Algorithme 2"""
def algo2(n, M, e):
    N = floor(n/M)
    pi = np.array([], dtype='f')
    for i in range(0,n-M,M):
        s=0
        for j in range(M):
            s += int(e[j+i])/M 
        pi = np.append(pi, s)
    ki_carre = 4*M*sum((pi-0.5)**2)
    P_value = sp.special.gammaincc(N/2, ki_carre/2)
    return P_value
    
#a = algo2(100, 10, "1100100100001111110110101010001000100001011010001100001000110100110001001100011001100010100010111000") fournit des erreurs d'approximations sur les fractions



## Histogramme des P_values
f = [algo1(i,epsilon) for i in range(1000,5000)]##1004882
def hist(f):
    frequence, lim, patches = plt.hist(f, range = (0, 1), bins = 10)
    plt.xlabel('Valeurs de P_value')
    plt.ylabel('Fréquence comptée')
    plt.title('Histogramme des P_values')
    plt.show()

## Diagramme circulaire des P_values
def circ(f):
    name = ['[0;0.1]', '[0.1;0.2]', '[0.2;0.3]', '[0.3;0.4]', '[0.4;0.5]', '[0.5;0.6]', '[0.6;0.7]','[0.7;0.8]', '[0.8;0.9]', '[0.9;1]']
    frequence = [sum(0.1*i<=num<0.1*(i+1) for num in f) for i in range(10)]
    plt.pie(frequence, labels=name, autopct='%1.1f%%', startangle=90)
    plt.title('Camembert des P_values')
    plt.show()

## Courbe de répartition des P_values
def curve(f):
    plt.figure(1)		# je crée une figure dont le numéro 1
    x = [i/10 for i in range(10)]   
    frequence = [sum(0.1*i<=num<0.1*(i+1) for num in f) for i in range(10)]
    plt.plot(x, frequence, 'r')	
    plt.xlabel('Valeurs de P_value')
    plt.ylabel('Fréquence comptée')
    plt.title('Courbe des P_values')
    plt.show()		

##Interface Graphique
fenetre = Tk()
fenetre.title('Sure or not Sure That is the Question?')

"""Lignes de saisies"""

Label1 = Label(fenetre, text = 'Input Data File :')
Label1.pack(side = LEFT, padx = 5, pady = 5)
File= StringVar()
Champ1 = Entry(fenetre, textvariable= File, bg ='bisque', fg='maroon')
Champ1.focus_set()
Champ1.pack(side = LEFT, padx = 5, pady = 5)


Label2 = Label(fenetre, text = 'BitStream length :')
Label2.pack(side = LEFT, padx = 5, pady = 5)
bsl= StringVar()
Champ2 = Entry(fenetre, textvariable= bsl, bg ='bisque', fg='maroon')
Champ2.focus_set()
Champ2.pack(side = LEFT, padx = 5, pady = 5)


Label3 = Label(fenetre, text = 'Number of Bitestream :')
Label3.pack(side = LEFT, padx = 5, pady = 5)
bsl= StringVar()
Champ3 = Entry(fenetre, textvariable= bsl, bg ='bisque', fg='maroon')
Champ3.focus_set()
Champ3.pack(side = LEFT, padx = 5, pady = 5)


Label4 = Label(fenetre, text = 'Number of Block :')
Label4.pack(side = LEFT, padx = 5, pady = 5)
nob= StringVar()
Champ4 = Entry(fenetre, textvariable= nob, bg ='bisque', fg='maroon')
Champ4.focus_set()
Champ4.pack(side = LEFT, padx = 5, pady = 5)


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
b1 = Button(text='Lancer', command=Executer)
b1.pack()
lbl1 = Label()
lbl1.pack()
 

