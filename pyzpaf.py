#!/usr/bin/env python
#-*- coding: utf-8 -*-

from math import *
from decimal import Decimal
import matplotlib.pyplot as plt
import numpy as np
import scipy as sp
from numpy.linalg import matrix_rank

from scipy import special
from itertools import groupby
from tkinter import *
from tkinter.messagebox import *



#fichier = open("C:/Users/Azoulay/Desktop/PAF-incertitude/matlab.txt", "r")
#fichier = open("C:/Users/Azoulay/Desktop/PAF-incertitude/data.txt", "r")
#epsilon = fichier.read()[3:]
#fichier.close()

################## Implémentation des algorithmes  #######################

""" Algorithme 1 : Frequency (Monobit) Test  """

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
    for i in range(0,N*M,M):
        s=0
        for j in range(M):
            s += int(e[j+i])/M 
        pi = np.append(pi, s) # vecteur des proportions de 1 dans chaque bloc 
    ki_carre = 4*M*sum((pi-0.5)**2)
    P_value = sp.special.gammaincc(N/2, ki_carre/2)
    return P_value
    
#a = algo2(100, 10, "1100100100001111110110101010001000100001011010001100001000110100110001001100011001100010100010111000") fournit des erreurs d'approximations sur les fractions

""" Algorithme 5: Binary Matrix Rank Test """

def binaryMatrixTest(n,e,M,Q): # e séquence binaire 
    epsilon= np.array([int(x) for x in list(e)]) # conversion string (entrée) en vecteur epsilon 
    print(epsilon)
    N= n//(Q*M)
    slice=Q*M # taille choisie pour le découpage de la séquence binaire 
    Ranks=[]
    Ranks += [matrix_rank(np.reshape(epsilon[0:slice],(M,Q)))] 
    # rang des matrices formées par les blocs du découpage rangés dans une liste
    for k in range(1,N):
        Ranks +=[matrix_rank(np.reshape(epsilon[k*slice +1 :(k+1)*slice+1],(M,Q)))]
#    print(Ranks) 
    
    FM=0
    FM_1=0
    #comptage des rangs valant M et M-1
    for i in range(len(Ranks)):
        if(Ranks[i]==M):
            FM +=1
        if(Ranks[i]==M-1):
            FM_1 +=1
            
    ki_carre= ((FM-0.2888*N)**2)/(0.2888*N)+(FM_1-0.5776*N)**2/(0.5776*N)+((N-FM-FM_1-0.1336*N)**2)/(0.1336*N)
    P_value= np.exp((-1)*ki_carre/2)
#    print(P_value)
    return P_value 

#for testing    
#epsi= "01011001001010101101"
#binaryMatrixTest(20,epsi,3,3)

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
   # print("N0=", N0)
    N1=0    # pour le nombre de pics du module de la TFD
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
def NonOverlappingTemplateMatching(n,B, e):
    M = int(n/8) #N=8 doit être <100
    N=8
    m = len(B) # m se doit d'être environ égale à 9 ou 10 
    w = [0]*N
    for i in range(N):
        block = e[i*M:(i+1)*M]
        j = 0
        while j < M-m+1:
            if(B == block[j:j+m]):
                w[i] += 1
                j += m
            else : 
                j += 1
    mu = (M - m +1)/2**m
    sigma_carre = M*(1/2**m - (2*m-1)/2**(2*m))
    ki_carre = sum([(wi-mu)**2 for wi in w])/sigma_carre
    P_value = sp.special.gammaincc(N/2 , ki_carre/2)
    return P_value


""" Algorithme 8: Overlapping Template Matching Test """

def delta(l,u):
    res = sum([1/2**k*sp.special.binom(k-1,l-1) for k in range(1,6)])
    return res

#il faut que n>10**6
def OverlappingTemplateMatching(n,B, e):
    m = len(B) #m environ égale à log_2(M) soit 9 ou 10
    K = 5
    M = 1032
    N = 968
    v = [0]*(K+1)
    for i in range(N):
        block = e[i*M:(i+1)*M]
        cpt = 0
        for j in range(M-m+1):
            cpt += (B == block[j:j+m])
        if(cpt>=5):
            v[5]+=1
        else:
            v[cpt]+=1
    lameda = (M-m+1)/2**m
    eta = lameda/2
    pi_5 = exp(-eta)*sum([eta**l/np.math.factorial(l)*delta(l,5) for l in range(1,6)])
    pi = [exp(-eta),eta/2*exp(-eta), exp(-eta)*eta/8*(eta+2),exp(-eta)*eta/8*(eta**2/6+eta+1),exp(-eta)*eta/16*(eta**3/24+eta**2/2+3*eta/2+1),pi_5]
    ki_carre = sum([(v[0]-N*pi[0])**2/(N*pi[0]),(v[1]-N*pi[1])**2/(N*pi[1]),(v[2]-N*pi[2])**2/(N*pi[2]),  
                    (v[3]-N*pi[3])**2/(N*pi[3]),(v[4]-N*pi[4])**2/(N*pi[4]),(v[5]-N*pi[5])**2/(N*pi[5])])
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
       


#################### Représentations graphiques #############################

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


#str = "000000001\n000000011\n000000101\n000000111\n000001001\n000001011\n000001101\n000001111\n000010001\n000010011\n000010101\n000010111\n000011001\n000011011\n000011101\n000011111\n000100011\n000100101\n000100111\n000101001\n000101011\n000101101\n000101111\n000110011\n000110101\n000110111\n000111001\n000111011\n000111101\n000111111\n001000011\n001000101\n001000111\n001001011\n001001101\n001001111\n001010011\n001010101\n001010111\n001011011\n001011101\n001011111\n001100101\n001100111\n001101011\n001101101\n001101111\n001110101\n001110111\n001111011\n001111101\n001111111\n010000011\n010000111\n010001011\n010001111\n010010011\n010010111\n010011011\n010011111\n010100011\n010100111\n010101011\n010101111\n010110011\n010110111\n010111011\n010111111\n011000111\n011001111\n011010111\n011011111\n011101111\n011111111\n100000000\n100010000\n100100000\n100101000\n100110000\n100111000\n101000000\n101000100\n101001000\n101001100\n101010000\n101010100\n101011000\n101011100\n101100000\n101100100\n101101000\n101101100\n101110000\n101110100\n101111000\n101111100\n110000000\n110000010\n110000100\n110001000\n110001010\n110010000\n110010010\n110010100\n110011000\n110011010\n110100000\n110100010\n110100100\n110101000\n110101010\n110101100\n110110000\n110110010\n110110100\n110111000\n110111010\n110111100\n111000000\n111000010\n111000100\n111000110\n111001000\n111001010\n111001100\n111010000\n111010010\n111010100\n111010110\n111011000\n111011010\n111011100\n111100000\n111100010\n111100100\n111100110\n111101000\n111101010\n111101100\n111101110\n111110000\n111110010\n111110100\n111110110\n111111000\n111111010\n111111100\n111111110"

#
template_9= str.split('\n')
"""
les_f = [[NonOverlappingTemplateMatching(10000,t,epsilon[i:i+10000]) for i in range(0,1000000,10000)] for t in template_9]

result = [P_value_T(f) for f in les_f]

"""


    

