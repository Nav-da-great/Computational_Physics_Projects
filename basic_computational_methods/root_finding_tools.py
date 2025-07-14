from math import *

# Must define a function f(x) before using any of these functions

def bisection(f, a, b, tolerance = 1e-6):
    if f(a) * f(b) >= 0:
        raise ValueError("Selected values do not have the root between them")

    dx = abs(a - b)

    while dx > tolerance:
        c = (a + b) / 2
        if f(a) * f(c) < 0:
            b = c
        else:
            a = c
        dx = abs(a - b)
    return c

def newton(f , df, a, tolerance = 1e-6):
    dx = 2 * tolerance

    while dx > tolerance:
        b = a - (f(a) / df(a))
        dx = abs(b - a)
        a = b
    return a

def secant(f, a, b, tolerance = 1e-6):
    dx = abs(a - b)
    
    while dx > tolerance:
        m = (f(b) - f(a)) / (b - a)
        c = b - (f(b) / m)
        a = b
        b = c
        dx = abs(a - b)
    return c