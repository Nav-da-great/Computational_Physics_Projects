from vpython import *
from basics_of_vpython.tools import Simulation

sim = Simulation()
canvas(width = 1900, height = 600)

length_1 = 10
length_2 = 5

spring_constant = 1e6

theta_1 = 90 * (pi / 180)
theta_2 = 0 * (pi / 180)

origin = sphere(pos = vector(0, 10, 0), radius = 0)

bob_1_initial = (length_1 * vector(sin(theta_1), -cos(theta_1), 0)) + origin.pos
bob_1 = sphere(pos = bob_1_initial, radius = 1, color = color.red, make_trail = True, retain = 400)
bob_1.mass = 1
bob_1.momentum = bob_1.mass * vector(0, 0, 0)

bob_2_initial = (length_2 * vector(sin(theta_2), -cos(theta_2), 0)) + bob_1.pos
bob_2 = sphere(pos = bob_2_initial, radius = 1, color = color.blue, make_trail = True, retain = 400)
bob_2.mass = 1
bob_2.momentum = bob_2.mass * vector(0, 0, 0)

spring_1 = cylinder(pos = origin.pos, axis = bob_1.pos - origin.pos, radius = 0.1)
spring_2 = cylinder(pos = bob_1.pos, axis = bob_2.pos - bob_1.pos, radius = 0.1)

gravity = 9.8 * vector(0, -1, 0)

def binds(evt):
    if evt.id == "g":
        gravity.y = -evt.value
        g_text.text = f"Value of gravity is: {evt.value}m/s2"
    elif evt.id == "mass1":
        bob_1.mass = evt.value
        m_1_text.text = f"Mass of red bob is {evt.value}kg"
    elif evt.id == "mass2":
        bob_2.mass = evt.value
        m_2_text.text = f"Mass of blue bob is {evt.value}kg"

wtext(text = "\n" + "Vary the mass of the red bob")
wtext(text = "\n")
mass_1_change = slider(bind = binds, min = 1, max = 20, step = 0.01, value = bob_1.mass, id = "mass1")
m_1_text = wtext(text = "Mass is: {:.2f}kg".format(bob_1.mass))

wtext(text = "\n" + "Vary the mass of the blue bob")
wtext(text = "\n")
mass_2_change = slider(bind = binds, min = 1, max = 20, step = 0.01, value = bob_1.mass, id = "mass2")
m_2_text = wtext(text = "Mass is: {:.2f}kg".format(bob_2.mass))

wtext(text = "\n" + "Vary the value of gravity")
wtext(text = "\n")
gravity_change = slider(bind = binds, max = 20, min = 0, step = 0.01, value = -gravity.y, id = "g")
g_text = wtext(text = "Gravity is: {:.2f}m/s2".format(-gravity.y))

# ========================================== Pause button section ========================================== #
wtext(text = "\n\n")
pause_button = button(bind = sim.pause_bind, text = "Play", background = color.green, color = color.white)

# ========================================== Exit button section ========================================== #

wtext(text = " ")
exit_button = button(bind = sim.exit_bind, text = "Exit simulation", background = color.red, color = color.white)

# ========================================== Physical simulation section ========================================== #

dt = 0.0001
while sim.running:
    rate(10000)

    if not sim.pause:
        L_1 = bob_1.pos - origin.pos
        L_2 = bob_2.pos - bob_1.pos

        bob_1.v_tangential = (bob_1.momentum / bob_1.mass)
        bob_2.v_tangential = (bob_2.momentum / bob_2.mass)

        bob_1.v_radial = norm(L_1) * dot(bob_1.v_tangential, norm(L_1))
        bob_2.v_radial = norm(L_1) * dot(bob_2.v_tangential, norm(L_1))

        spring_1.force = -spring_constant * (mag(L_1) - length_1) * norm(L_1)
        spring_2.force = -spring_constant * (mag(L_2) - length_2) * norm(L_2)
        
        force_1 = (bob_1.mass * gravity) + spring_1.force - spring_2.force
        force_2 = (bob_2.mass * gravity) + spring_2.force

        bob_1.momentum += force_1 * dt
        bob_1.pos += (bob_1.momentum / bob_1.mass) * dt
        spring_1.axis = bob_1.pos - origin.pos

        bob_2.momentum += force_2 * dt
        bob_2.pos += (bob_2.momentum / bob_2.mass) * dt
        
        spring_2.pos = bob_1.pos
        spring_2.axis = bob_2.pos - bob_1.pos
