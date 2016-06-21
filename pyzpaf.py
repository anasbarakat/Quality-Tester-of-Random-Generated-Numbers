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

fichier = open("C:/Users/Azoulay/Desktop/PAF-incertitude/data.txt", "r")
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

""" Algorithme 6: Discrete Fourier Transform (Spectral) Test """

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

#print(testDCTalgo(10,epsilon1))


""" Algorithme 10: Linear Complexity Test """

def berkelamp_massey(tab, M):
    b = [1] +[0]*(M-1)
    c = [1] +[0]*(M-1)
    t = []
    l = 0
    m = -1
    for n in range(M):
        d = 0
        for i in range(l+1):
            d ^= c[i] * int(tab[n - i])
        if (d==1):
            t = c[:] 
            M_N = n - m
            for j in range(M - M_N):
                c[M_N +j] ^= b[j]
            if(l <= n/2):
                l = n + 1 - l
                m = n
                b = t[:]
    return l
      
    
def algo10(n,M, e):
    mu = (M/2 + 10/36 - (M/3+2/9)/2**M) if M % 2 == 1 else (M/2 + 8/36 - (M/3+2/9)/2**M)
    T = 0
    N = int (n/M)
    v = [0,0,0,0,0,0,0]
    for i in range(0,n-M,M):
        L = berkelamp_massey(e[i:i+M], M)
        T = -(L-mu)+2/9 if M % 2 == 1 else (L-mu)+2/9
        if (T <= -2.5):
            v[0]+= 1
        elif(T<=-1.5):
            v[1]+= 1
        elif(T<=-0.5):
            v[2]+= 1
        elif(T<=0.5):
            v[3]+= 1
        elif(T<=1.5):
            v[4]+= 1
        elif(T<=2.5):
            v[5]+= 1
        else:
            v[6]+= 1
    ki_carre = sum([(v[0]-N*0.010417)**2/(N*0.010417),(v[1]-N*0.03125)**2/(N*0.03125),(v[2]-N*0.125)**2/(N*0.125),  
                    (v[3]-N*0.5)**2/(N*0.5),(v[4]-N*0.25)**2/(N*0.25),(v[5]-N*0.0625)**2/(N*0.0625), (v[6]-N*0.020833)**2/(N*0.020833)])
    P_value = P_value = sp.special.gammaincc(3, ki_carre/2)
    return P_value
            
#a = algo10(1000000,1000, epsilon[:1000000])        
        


## Histogramme des P_values

#f = [algo1(1000,epsilon[i:i+1000]) for i in range(1000,50000,1000)]##1004882

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

## Pourcentage des Tests Réussis
def percent(f):
    n = len(f)
    s = 0
    for i in range(n):
        if(f[i]>0.01):
            s +=1
    return s/n
