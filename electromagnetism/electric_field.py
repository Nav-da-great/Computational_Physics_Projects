from vpython import *
from utilities.tools import Simulation

# Simulation of a changing electric field between two moving/stationary charged particles

canvas(width = 1900, height = 800, background = color.black, title = "<h1>Changing electric field between two charged particles</h1>")
sim = Simulation()

# ========================================== Exit button section ========================================== #

wtext(text = "\n" + " " * 177)
exit_button = button(bind = sim.exit, text = "Exit simulation", background = color.red, color = color.white)

# ========================================== Physical simulation section ========================================== #

k = 9e9
Q = 1
q = 1

charge_Q = sphere(pos = vector(-0.4, 0, 0), radius = 0.1, color = color.blue)
charge_q = sphere(pos = vector(0.4, 0, 0), radius = 0.1, color = color.yellow)

charge_Q.v = vector(0.03, 0, 0)
charge_q.v = vector(-0.03, 0, 0)

field_array = []
max_strength_of_field = 1e11

t = 0
dt = 1/60

# Create a rectangular plane of position vectors of test charges centered at the origin
def rectangle_maker(rows, cols, spacing = 2):
    width = (cols - 1) * spacing
    height = (rows - 1) * spacing
    begin = vector(-width / 2, -height / 2, 0)
    positions = []
    for i in range(rows):
        for j in range(cols):
            pos = begin + vector(j * spacing, i * spacing, 0)
            positions.append(pos)
    return positions

position_array = rectangle_maker(20, 30, 0.05)

# Using vector(0, 0, 0) as a dummy value to populate the array, will be handled with real values in animation loop
field_array = [arrow(pos = vec, axis = vector(0, 0, 0), color = color.red, shaftwidth = 0.005) for vec in position_array] 

# ========================================== Animation loop ========================================== #

frame_count = 0

while sim.running:

    rate(60)    # 60 calculations per second ceiling
    # Update positions of both charges if they have a velocity
    charge_Q.pos += charge_Q.v * dt
    charge_q.pos += charge_q.v * dt

    # Temporal decimation: Do not need to animate charges every frame the ball moves thus saving compute power
    if frame_count % 4 == 0:

    # Populate field_array with calculated values of net electric field
        for i in range(len(field_array)):

            # Calculating vector positions between a point in plane and charge
            electric_field_vector_1 = position_array[i] - charge_Q.pos
            electric_field_vector_2 = position_array[i] - charge_q.pos

            # Calculating electric field vectors
            E_1 = (k * Q) * norm(electric_field_vector_1) / mag2(electric_field_vector_1)
            E_2 = (k * q) * norm(electric_field_vector_2) / mag2(electric_field_vector_2)
            E = E_1 + E_2

            if mag(E) != 0:
                scale = 0.05 / mag(E)
            else:
                scale = 0   # Edge-case where electric field is equal and opposite (throws division by 0 if not handled)

            strength = mag(E)
            norm_strength = min(1, strength / max_strength_of_field) # Normalize max_strength since color vector does not accept value > 1 as args

            field_array[i].axis = E * scale
            field_array[i].color = vector(norm_strength, 0, 1 - norm_strength)

    frame_count += 1

