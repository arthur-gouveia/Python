# -*- coding: utf-8 -*-
"""
Created on Thu Sep  1 23:20:32 2016

@author: Arthur Gouveia

Calculates the roots of a second degree equation of the form ax²+bx+c

The code requests the user to input the a, b and c values and then prints
the equation roots

In case the user inputs non numerical values for a, b or c the code raises
an exception and asks the user to input the values again.
"""
from math import sqrt

while True:
    try:
        a = float(input('Input a: '))
        b = float(input('Input b: '))
        c = float(input('Input c: '))
        #If no exception is thrown the while loop breaks
        break
    except ValueError:
        print("Incorrect value. Input a number.")

#Calculates the value of Delta
delta = b ** 2 - 4 * a * c

if delta == 0:
#if Delta equals 0 the equation has only one root
    x1 = (sqrt(delta) - b) / (2 * a)
    print("The only root of the equation %.2fx^2 + %.2fx + %.2f is %.3f" 
             %(a, b, c, x1))
elif delta > 0:
#If Delta is bigger tnan zero the equation has two roots
    x1 = (sqrt(delta) - b) / (2 * a)
    x2 = (-sqrt(delta) - b) / (2 * a)
    print("The roots of the equation %.2fx^2 + %.2fx + %.2f are %.3f and %.3f"
          %(a, b, c, x1, x2))
elif delta < 0:
#If Delta less than zero the equation has no real roots
    print("The equation %.2fx^2 + %.2fx + %.2f has no real roots." %(a, b, c))
