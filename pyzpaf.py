#!/usr/bin/env python
#-*- coding: utf-8 -*-

from math import *
from decimal import Decimal
import matplotlib.pyplot as plt
import numpy as np
import scipy as sp
from scipy import special
from itertools import groupby
from tkinter import *
from tkinter.messagebox import *


fichier = open("C:/Users/Azoulay/Desktop/PAF-incertitude/data.txt", "r")
epsilon = fichier.read()[3:]

#fichier = open("/Users/anasbarakat/Documents/PAF-incertitude/data.txt", "r")
#epsilon = fichier.read()[3:]

fichier.close()

#n = int(input("Entrée la longueur n : "))

## Implémentations des Algorithmes


"""    Algorithme 1 : Frequency (Monobit) Test  """
def frequencyTest(n, e):# n longueur de la séquence, e séquence de bits
    S_n = 0
    for i in range(n):
        S_n += 2*int(e[i])-1   # calcul du nombre de 1 en plus que de 0 
    s_obs = abs(S_n)/sqrt(n)
    P_value = erfc(s_obs/sqrt(2))
    return P_value


""" Algorithme 2: Frequency Test within a Block"""

def frequencyTestBlock(n, M, e): # n longueur de la séquence, M taille d'un block, 
# e séquence de bits
    N = floor(n/M) 
    pi = np.array([], dtype='f')
    for i in range(0,n-M,M):
        s=0
        for j in range(M):
            s += int(e[j+i])/M 
        pi = np.append(pi, s) # vecteur des proportions de 1 dans chaque bloc 
    ki_carre = 4*M*sum((pi-0.5)**2)
    P_value = sp.special.gammaincc(N/2, ki_carre/2)
    return P_value
    
#a = algo2(100, 10, "1100100100001111110110101010001000100001011010001100001000110100110001001100011001100010100010111000") fournit des erreurs d'approximations sur les fractions

""" Algorithme 6: Discrete Fourier Transform (Spectral) Test """

epsilon1= [1,0,0,1,0,1,0,0,1,1]
epsilon2= [1,1,0,0,1,0,0,1,0,0,0,0,1,1,1,1,1,1,0,1,1,0,1,0,1,0,1,0,0,0,1,0,0,0,1,0,0,0,0,
           1,0,1,1,0,1,0,0,0,1,1,0,0,0,0,1,0,0,0,1,1,0,1,0,0,1,1,0,0,0,1,0,0,1,1,0,0,0,1,1,0,0,1,1,0,0,0,1,0,1,0,0,0,1,0,1,1,1,0,0,0]

#conversion des 0 en -1 
def epsilonToX(n, epsilon): # epsilon séquence, n longueur de la séquence
    
    X = []
    for i in range(n):
        X += [2*int(epsilon[i])-1]
    #print(X)
    return X
    
 # calcul de la transformée de Fourier discrète et module       
def DFT(n,X):  
    
    S= np.fft.fft(X)
    Sbis= S[:int(n/2)]
    #print("Sbis=", Sbis)
    Mod=[]
    
    for k in range(len(Sbis)):
        Mod += [abs(Sbis[k])]
    return Mod

# calcul de P_value       
def P_value(n, epsilon):
    T= sqrt(log(1/0.05)*n) # valeur du seuil de décision sur le module 
   # print("T=", T)
    N0=0.95*n/2  # valeur de référence (au seuil de 95%) 
    # pour le nombre de pics du module de la TFD 
   # print("N0=", N0)
    N1=0    
    M= DFT(n,epsilonToX(n, epsilon))
   # print("M=", M)
    
    for k in range(len(M)): # pour le calcul du nombre de modules < T 
        if (M[k]<T):
            N1 +=1
    
   # print("N1=", N1 )
    
    d= (N1-N0)/(sqrt(n*(0.95)*(0.05)/4))
   # print("d=", d)
    P_value= erfc(abs(d)/sqrt(2))
   # print("P_value=", P_value)

    return P_value
 
# randomness test   
def testDCT(n, epsilon):  
    Pvalue= P_value(n, epsilon)
    if (Pvalue < 0.01):
        return "The sequence is NON-RANDOM"
    else: 
        return "The sequence is RANDOM"

#print(testDCTalgo(10,epsilon1))

""" Algorithme 7: Non-Overlapping Template Matching Test """
#S'assurer que M>0.01*n
def NonOverlappingTemplateMatching(n,M, B, e):
    N = int(n/M) #N doit être <100
    m = len(B) # m se doit d'être environ égale à 9 ou 10 
    w = [0]*N
    for i in range(N):
        block = e[i:i+M]
        j = 0
        while j < M-m+1:
            if(B == block[j:j+m]):
                w[i] += 1
                j += m
            else : 
                j += 1
    mu = (M - m +1)/2**m
    sigma_carre = M*(1/2**m - (2*m-1)/2**(2*m))
    ki_carre = sum([(wi-mu)**2/sigma_carre for wi in w])
    P_value = sp.special.gammaincc(N/2 , ki_carre/2)
    return P_value


""" Algorithme 8: Overlapping Template Matching Test """

#il faut que n>10**6
def OverlappingTemplateMatching(n,B, e):
    m = len(B) #m environ égale à log_2(M) soit 9 ou 10
    K = 5
    M = 1032
    N = 968
    v = [0]*(K+1)
    for i in range(N):
        block = e[i:i+M]
        cpt = 0
        for j in range(M-m+1):
            cpt += (B == block[j:j+m])
        if(cpt>=5):
            v[5]+=1
        else:
            v[cpt]+=1
    lameda = (M-m+1)/2**m
    eta = lameda/2
    ki_carre = sum([(v[0]-N*0.364091)**2/(N*0.364091),(v[1]-N*0.185659)**2/(N*0.185659),(v[2]-N*0.139381)**2/(N*0.139831),  
                    (v[3]-N*0.100571)**2/(N*0.100571),(v[4]-N*0.070432)**2/(N*0.070432),(v[5]-N*0.166269)**2/(N*0.166269)])
    P_value = sp.special.gammaincc(5/2 , ki_carre/2)
    return P_value


""" Algorithme 10: Linear Complexity Test """

# algorithme pour la détermination
#  de la complexité linéaire d'un block tab de M bits
def berkelamp_massey(tab, M):   
    b = [1] +[0]*(M-1)
    c = [1] +[0]*(M-1)
    t = []
    l = 0
    m = -1
    for n in range(M):
        d = 0
        for i in range(l+1):
            d ^= c[i] * int(tab[n - i]) # ^ opérateur XOR 
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
      
    
def linearComplexityTest(n,M, e):
    depowm = 2**M
    mu = (M/2 + 10/36 - (M/3+2/9)/depowm) if M % 2 == 1 else (M/2 + 8/36 - (M/3+2/9)/depowm)
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
#f = [frequencyTest(1000,epsilon[i:i+1000]) for i in range(1000,50000,1000)]


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
    
def P_value_T(f):
    frequence = [sum(0.1*i<=num<0.1*(i+1) for num in f) for i in range(10)]
    s_10 = len(f)/10
    ki_carre = sum((f_i-s_10)**2/s_10 for f_i in frequence)
    p_value_t = sp.special.gammaincc(9/2,ki_carre/2)
    return p_value_t
