# -*- coding: utf-8 -*-
"""
Created on Tue Nov 26 16:40:05 2019

@author: MICEL
"""

xa = int (input ("Masukkan nilai x pada titik A:"))
ya = int (input ("Masukkan nilai y pada titik A:"))
xb = int (input ("Masukkan nilai x pada titik B:"))
yb = int (input ("Masukkan nilai y pada titik B:"))

def hitungx (xa, xb):
    x = xb - xa
    return x

def hitungy (ya, yb):
    y = yb - ya
    return y

def hitungjarak (x,y):
    from math import sqrt
    z = sqrt(x**2 + y**2)
    print (z)
    
print ()
print ("Jarak antara titik A dan titik B adalah")
hitungjarak (x,y)