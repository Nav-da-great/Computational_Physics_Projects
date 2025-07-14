from math import *

# Must define a function f(x) before using any of these functions

def derivative_simple(f, a, dx = 0.001):
    return (f(a + dx) - f(a)) / (dx)

def derivative_three_point(f, a, dx = 0.001):   # Better accuracy than simple derivative, works best on noisy data
    return (f(a + dx) - f(a - dx)) / (2 * dx)

def derivative_five_point(f, a, dx = 0.001):    # Works best for smooth functions
    return (f(a - 2 * dx) - 8 * f(a - dx) + 8 * f(a + dx) - f(a + 2 * dx)) / (12 * dx)