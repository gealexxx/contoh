# -*- coding: utf-8 -*-
"""
Created on Tue Nov 26 16:19:38 2019

@author: MICEL
"""

xa = int (input ("Masukkan nilai x pada titik A:"))
ya = int (input ("Masukkan nilai y pada titik A:"))
xb = int (input ("Masukkan nilai x pada titik B:"))
yb = int (input ("Masukkan nilai y pada titik B:"))

x = xb - xa
y = yb - ya

from math import sqrt
z = sqrt(x**2 + y**2)

print ()
print ("Jarak antara titik A dan titik B adalah", z)