#!/usr/bin/env python
#-*- coding: utf-8 -*-

from math import *
import matplotlib.pyplot as plt
import numpy as np

fichier = open("C:/Users/Azoulay/Downloads/paf.txt", "r")
epsilon = fichier.read()[3:]
fichier.close()

n = int(input("Entrée la longueur n : "))

"""    Algorithme 1  """
def algo1(n):
    S_n = 0
    for i in range(n):
        S_n += 2*int(epsilon[i])-1
    s_obs = abs(S_n)/sqrt(n)
    P_value = erfc(s_obs/sqrt(2))
    return P_value

""" Algorithme 2"""
def algo2(n, M):
    N = floor(n/M)
    pi = []
    for i in range(N):
        for j in range(3):
            pi += [ 


## Histogramme des P_values
f = [algo1(i) for i in range(1000,10000)]##1004882
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
circ(f)