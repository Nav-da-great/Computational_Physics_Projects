from vpython import *

# Simulation of elastic collision of two blocks and a wall

mass_large = 10000
mass_small = 1
k1 = 1e5
k2 = k1
l_eq = 0.05

g = graph(width = 400, height = 400)
f = gcurve(color = color.red)

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

while True:
    rate(1e5)

    l_box = largeBox.pos.x - smallBox.pos.x # Horizontal distance between the blocks
    l_wall = smallBox.pos.x - wall.pos.x    # Horizontal distance between the small block and the wall

    force_large = vector(0, 0, 0)
    force_small = vector(0, 0, 0)

    if (l_box < (largeBox.size.x / 2) + (smallBox.size.x / 2)):
        force_large = k1 * (l_box - l_eq) * vector(1, 0, 0) # Normal force along x-axis
        force_small = -force_large
        
        if not box_colliding:
            count += 1
            box_colliding = True
    else:
        box_colliding = False


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

    # f.plot(largeBox.p.x / mass_large, smallBox.p.x / mass_small)
    
    t += dt