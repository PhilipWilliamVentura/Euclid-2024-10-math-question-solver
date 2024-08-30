#Euclid 2024 math comp. question #10

# Suppose that s and t are real numbers with 0 < s ≤ 1 and 0 < t ≤ 1. 
# PointsA(−1, 0), B(0, 4) and C(1, 0) form 4ABC. Points S(s, 0) and T(−t, 0) lie on AC.
# Point P lies on AB and point Q lies on BC, with neither P nor Q at a vertex of triangle ABC
# Line segments SP and T Q intersect at X and partition 4ABC into four regions. 
# For some such pairs (s, t) of real numbers and points P and Q, the line segments SP and T Q in fact partition triangle ABC into four regions of equal area. 
# We call such a pair (s, t) a balancing pair.
# (a) Suppose that (s, t) is a balancing pair with s = 1 and that line segments SP and TQ partition triangle ABC into four regions of equal area. Determine the coordinates of P.
# (b) Prove that there exist real numbers d, e, f, and g for which all balancing pairs (s, t) satisfy an equation of the form:
# s^2 + t^2 = dst + es + ft + g 
# and determine the values of d, e, f, and g.

import sympy as spm
import numpy as np
from fractions import Fraction
from sympy import simplify, symbols, factor, Rational

# Input coordinates for points A, B, and C
Ax, Ay = int(input("Point A, x coordinate:")), int(input("Point A, y coordinate:"))
Bx, By = int(input("Point B, x coordinate:")), int(input("Point B, y coordinate:"))
Cx, Cy = int(input("Point C, x coordinate:")), int(input("Point C, y coordinate:"))

# Area of triangle ABC
surfaceABC = 0.5 * abs((Cx - Ax) * By)
surfaceregion = surfaceABC / 4

# Paramaters of an equation
def equation(x1, y1, x2, y2):
    m = (y2 - y1) / (x2 - x1)  
    k = y1 - m * x1  
    return m, k

# Value for x from an equation
def x_value_from_eq(y, x1, y1, x2, y2):
    m = (y2 - y1) / (x2 - x1)  
    k = y1 - m * x1  
    x = (y - k) / m
    return x

# Value for y from an equation
def y_value_from_eq(x, x1, y1, x2, y2):
    m = (y2 - y1) / (x2 - x1)  
    k = y1 - m * x1  
    y = m * x + k
    return y

# Intersection of the lines and the point's x value
def intersection(x1, y1, x2, y2, x3, y3, x4, y4):
    m1, k1 = equation(x1, y1, x2, y2)
    m2, k2 = equation(x3, y3, x4, y4)
    x = (k2 - k1) / (m1 - m2)
    return x
    
# (a)
def a():
    if Cy == Ay:
        Py = 2 * surfaceregion / (0.5 * abs(Cx - Ax))
        if Ay < Py < By:
            Px = x_value_from_eq(Py, Ax, Ay, Bx, By)
            print(f"a) P({Px}, {Py})")
    else:
        print("Not a balancing pair")

# (b)
def b():
        s, t = symbols('s t')
        Sx, Sy = s, Cy
        Tx, Ty = -t, Ay
        heightAPS = 4 / (Sx - Ax)
        heightSMT = 2 / (Sx - Tx)
        heightCQT = 4 / (Cx - Tx)
        Py = heightAPS
        Px = x_value_from_eq(Py, Ax, Ay, Bx, By)
        Qy = heightCQT
        Qx = x_value_from_eq(Qy, Bx, By, Cx, Cy)
        My1 = simplify(heightSMT)
        Mx = simplify(intersection(Px, Py, Sx, Sy, Tx, Ty, Qx, Qy))
        My2 = factor(simplify(y_value_from_eq(Mx, Px, Py, Sx, Sy)))
        target_My1 = Rational(2) / (s + t)
        target_My2 = 2.0 * (s + t) / (0.5 * s**2 + 1.0 * s + 0.5 * t**2 + 1.0 * t)
        if My1.equals(target_My1) and My2.equals(target_My2):
            print("-4*s*t + 2*s + 2*t = s**2 + t**2, where d=-4, e=2, f=2, g=0")
        else:
            print('Error')

user_input = input("Letter a or b? ")
if user_input == 'a':
    a()
elif user_input == 'b':
    b()
else:
    print('Not available option')
    

