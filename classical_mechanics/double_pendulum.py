from vpython import *
from basics_of_vpython.tools import Simulation

sim = Simulation()
canvas(width = 1900, height = 600)
wtext(text = "\n" + " " * 177)
exit_button = button(bind = sim.exit, text = "Exit simulation", background = color.red, color = color.white)

length_1 = 10
constant_1 = 10e3

length_2 = 5
constant_2 = 10e3

theta_1 = 60 * (pi / 180)
theta_2 = -60 * (pi / 180)

origin = sphere(pos = vector(0, 10, 0), radius = 0)

bob_1_initial = (length_1 * vector(sin(theta_1), -cos(theta_1), 0)) + origin.pos

bob_1 = sphere(pos = bob_1_initial, radius = 1, color = color.red, make_trail = True)
bob_1.mass = 1
bob_1.momentum = bob_1.mass * vector(0, 0, 0)

bob_2_initial = (length_2 * vector(sin(theta_2), -cos(theta_2), 0)) + bob_1.pos
bob_2 = sphere(pos = bob_2_initial, radius = 1, color = color.blue, make_trail = True)
bob_2.mass = 1
bob_2.momentum = bob_2.mass * vector(0, 0, 0)

spring_1 = cylinder(pos = origin.pos, axis = bob_1.pos - origin.pos, radius = 0.1)
spring_2 = cylinder(pos = bob_1.pos, axis = bob_2.pos - bob_1.pos, radius = 0.1)

gravity = 9.8 * vector(0, -1, 0)

dt = 0.01
while sim.running:
    rate(100)

    L_1 = bob_1.pos - spring_1.pos
    L_2 = bob_2.pos - bob_1.pos

    spring_1.force = -constant_1 * (mag(L_1) - length_1) * norm(L_1)
    spring_2.force = -constant_2 * (mag(L_2) - length_2) * norm(L_2)
    
    force_1 = (bob_1.mass * gravity) + spring_1.force - spring_2.force
    force_2 = (bob_2.mass * gravity) + spring_2.force

    bob_1.momentum += force_1 * dt
    bob_1.pos += (bob_1.momentum / bob_1.mass) * dt
    spring_1.axis = bob_1.pos - origin.pos

    bob_2.momentum += force_2 * dt
    bob_2.pos += (bob_2.momentum / bob_2.mass) * dt
    
    spring_2.pos = bob_1.pos
    spring_2.axis = bob_2.pos - bob_1.pos
