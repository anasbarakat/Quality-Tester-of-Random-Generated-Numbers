#!/usr/bin/env python
#-*- coding: utf-8 -*-

from math import *
import matplotlib.pyplot as plt
import numpy as np

"""
fichier = open("/Users/anasbarakat/Documents/PAF-incertitudeRepo/data.txt", "r")
#epsilon = fichier.read()[3:]

fichier.close()

n = int(input("Entrée la longueur n : "))

Algorithme 1  
def algo1(n):
    S_n = 0
    for i in range(n):
        S_n += 2*int(epsilon[i])-1
    s_obs = abs(S_n)/sqrt(n)
    P_value = erfc(s_obs/sqrt(2))
    return P_value

 Algorithme 2
def algo2(n, M):
    N = floor(n/M)
    pi = []
    for i in range(N):
        for j in range(3):
            pi += [ 

## Histogramme des P_values
f= [algo1(i) for i in range(1000,10000)]
def hist(f):
    frequence, lim, patches = plt.hist(f, range = (0, 1), bins = 10)
    plt.xlabel('Valeurs de P_value')
    plt.ylabel('Fréquence comptée')
    plt.title('Histogramme des P_values')
    plt.show()

## Diagramme circulaire
def circ(f):
    name = ['[0;0.1]', '[0.1;0.2]', '[0.2;0.3]', '[0.3;0.4]', '[0.4;0.5]', '[0.5;0.6]', '[0.6;0.7]', '[0.8;0.9]', '[0.9;1]']
    plt.pie(f, labels=name, autopct='%1.1f%%', startangle=90)
    plt.axis('equal')
    plt.show()
circ(f)"""


""" Algorithme 3: Discrete Fourier Transform (Spectra) Test """

epsilon1= [1,0,0,1,0,1,0,0,1,1]
epsilon2= [1,1,0,0,1,0,0,1,0,0,0,0,1,1,1,1,1,1,0,1,1,0,1,0,1,0,1,0,0,0,1,0,0,0,1,0,0,0,0,
           1,0,1,1,0,1,0,0,0,1,1,0,0,0,0,1,0,0,0,1,1,0,1,0,0,1,1,0,0,0,1,0,0,1,1,0,0,0,1,1,0,0,1,1,0,0,0,1,0,1,0,0,0,1,0,1,1,1,0,0,0]

def epsilonToX(n, epsilon):
    X = []
    for i in range(n):
        X += [2*int(epsilon[i])-1]
    print(X)
    return X
        
def DFT(n,X):
    
    S= np.fft.fft(X)
    Sbis= S[:int(n/2)]
    print("Sbis=", Sbis)
    Mod=[]
    
    for k in range(len(Sbis)):
        Mod += [abs(Sbis[k])]
    return Mod
        
def P_value(n, epsilon):
    T= sqrt(log(1/0.05)*n)
    print("T=", T)
    N0=0.95*n/2
    print("N0=", N0)
    N1=0    
    M= DFT(n,epsilonToX(n, epsilon))
    print("M=", M)
    
    for k in range(len(M)):
        if (M[k]<T):
            N1 +=1
    N1= N1-1
    print("N1=", N1 )
    
    d= (N1-N0)/(sqrt(n*(0.95)*(0.05)/4))
    print("d=", d)
    P_value= erfc(abs(d)/sqrt(2))
    print("P_value=", P_value)

    return P_value
    
def testDCTalgo(n, epsilon):
    Pvalue= P_value(n, epsilon)
    if (Pvalue < 0.01):
        return "The sequence is NON-RANDOM"
    else: 
        return "The sequence is RANDOM"

print(testDCTalgo(10,epsilon))


    
    


        
        
        





















