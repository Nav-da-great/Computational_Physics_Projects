from vpython import *
from tools import *

# Simulation of an elastic collision of two blocks and a wall

canvas(width = 600, height = 600, background = color.black, title = "<h1>Elastic collision of two blocks to calculate Pi</h1>")
sim = Simulation()

# ========================================== Exit button section ========================================== #

wtext(text="\n\n" + " " * 45)  # Space for visual centering
exit_button = button(bind = sim.exit, text = "Exit simulation", background = color.red, color = color.white)

# ========================================== Physical simulation section ========================================== #

mass_large = 10000
mass_small = 1
k1 = 1e5
k2 = k1
l_eq = 0.05

largeBox = box(pos = vector(0.2, 0.15, 0), size = vector(0.3, 0.3, 0.05), color = color.cyan)
smallBox = box(pos = vector(-0.3, 0.05, 0), size = vector(0.1, 0.1, 0.05), color = color.yellow)
wall = box(pos = vector(-0.75, 0.5, 0), size = vector(0.2, 1, 0.05))

largeBox.p = mass_large * vector(-0.075, 0, 0)
smallBox.p = mass_small * vector(0, 0, 0)

t = 0
dt = 1e-5

count = 0
box_colliding = False
wall_colliding = False

# ========================================== Animation loop ========================================== #

while sim.running:
    rate(1e5)

    l_box = largeBox.pos.x - smallBox.pos.x # Horizontal distance between the blocks
    l_wall = smallBox.pos.x - wall.pos.x    # Horizontal distance between the small block and the wall

    # Initialization of normal force vectors
    force_large = vector(0, 0, 0)
    force_small = vector(0, 0, 0)

    # Force between boxes
    if (l_box < (largeBox.size.x / 2) + (smallBox.size.x / 2)):
        force_large = k1 * (l_box - l_eq) * vector(1, 0, 0) # Normal force along x-axis
        force_small = -force_large
        
        if not box_colliding:
            count += 1
            box_colliding = True
    else:
        box_colliding = False

    # Force between box and wall
    if (l_wall < (smallBox.size.x / 2) + (wall.size.x / 2)):
        force_small = k2 * (l_wall - l_eq) * vector(1, 0, 0)

        if not wall_colliding:
            count += 1
            wall_colliding = True
    else:
        wall_colliding = False
        
        largeBox.p += force_large * dt
    largeBox.pos += (largeBox.p / mass_large) * dt

    smallBox.p += force_small * dt
    smallBox.pos += (smallBox.p / mass_small) * dt

    t += dt

# Additional remarks: By tweaking the values of of spring constants (and subsequently reducing dt to be computationally less intensive),
# one can plot the phase space of the x-components of the velocities of both blocks and notice that as collisions become more frequent
# the plot (by virtue of momentum conservation) tends to be bounded by a circle, thus yielding the answer pi    
