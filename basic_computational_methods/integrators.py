from math import *

# Must define a function f(x) before using any of these functions

def integrate_simple(f, a, b, N = 1000):
    dx = (abs(a - b)) / N
    count = 0
    I = 0
    x = a

    while count < N:
        I += f(x) * dx
        x += dx
        count += 1
    return I

def integrate_trapezoid(f, a, b, N = 1000):
    dx = (abs(a - b)) / N
    temp = 0
    count = 1
    x = a

    const = (f(a) + f(b)) / 2

    while count < N:
        temp += f(x)
        x += dx
        count += 1
    
    return (const + temp) * dx
        
            

