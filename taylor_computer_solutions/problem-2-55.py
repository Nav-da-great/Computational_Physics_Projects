import numpy as np
import matplotlib.pyplot as plt

# Code to plot the the functions of x and y in a crossed E and B field (y and z axes respectively)

v_xo = 5 # Initial velocity along x-axis
v_dr = 2 # Drift velocity, with a magnitude of E/B
w = 100 * (np.pi) # Angular frequency, i.e. qB/m
t = np.linspace(0, 0.1, 1000)

x = ((v_xo - v_dr) * np.sin(w * t)) / w + v_dr * t
y = ((v_xo - v_dr) * (np.cos(w * t) - 1)) / w

plt.figure(figsize=(8, 6))
plt.plot(x, y)
plt.xlabel('x position')
plt.ylabel('y position')
plt.title('Helical Drift Motion of a Charged Particle')
plt.grid(True)
plt.axis('equal')
plt.show()