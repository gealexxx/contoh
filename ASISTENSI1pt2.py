# -*- coding: utf-8 -*-
"""
Created on Fri Nov 29 08:02:13 2019

@author: MICEL
"""

def BinToDec(binary):
    decimal = 0
    power = 0
    while binary > 0:
        decimal += 2**power*(binary%10)
        binary //= 10
        power += 1
    return decimal
binary = int(input("Masukkan Bilangan Biner : "))
print ("Decimal : ", str(BinToDec(binary)))
print ("Nilai desimal dari", binary, "adalah ", BinToDec(binary))