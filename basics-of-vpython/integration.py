from vpython import *

#Calculating moment of inertia of a uniform solid disc about its center

m = 0.5
r = 0.1

dx = 0.0001

phi = 0
dphi = 0.001

I = 0
sigma = (m / (pi * r**2))
temp = 0

while phi < 2 * pi:
    x = 0
    while x < r:
        dI = (sigma) * (x**3) * dx * dphi
        I += dI
        x += dx
    phi += dphi

print("Numerically integrated value = ", I)
print("Theoretical value = ", 0.5 * m * r**2)
