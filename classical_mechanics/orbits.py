from vpython import *

graph1 = graph(xtitle = 'time', ytitle = 'Energy')
kinetic_energy = gcurve(color = color.red, label = 'Kinetic Energy')
potential_energy = gcurve(color = color.blue, label = 'Potential Energy')
total_energy = gcurve(color = color.yellow, label = 'Total Energy')

G = 6.67e-11 # Universal constant of gravitation
Me = 5.97e25 # Mass of Earth
Re = 6.37e6 # Radius of the Earth

earth = sphere(pos = vector(0, 0, 0), radius = Re, texture = textures.earth)
satellite = sphere(pos = vector(2*Re, 0, 0), radius = Re/30, make_trail = True)

satellite.mass = 1000

vorbital = sqrt(G * Me / (2 * Re))

satellite.momentum = vector(0, vorbital, 0) * satellite.mass
print(vorbital)

t = 0
dt = 10

while True:
    rate(200)

    r = satellite.pos - earth.pos

    gravitational_force = -((G * Me * satellite.mass) / mag2(r)) * norm(r)
    satellite.momentum += gravitational_force * dt
    satellite.pos += (satellite.momentum / satellite.mass) * dt

    K = mag2(satellite.momentum) / (2 * satellite.mass)
    U = -(G * Me * satellite.mass) / (mag(r))
    E = K + U

    kinetic_energy.plot(t, K)
    potential_energy.plot(t, U)
    total_energy.plot(t, E)
    t += dt