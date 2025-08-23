from vpython import *
from utilities.tools import Simulation

canvas(Title = "<h1>Solution to problem 3.23 from Taylor's Classical Mechanics</h1>")
sim = Simulation()

graph = graph(title = "Trajectory of grenade", xtitle = "x-axis", ytitle = "y-axis", ymax = 20, ymin = -20, xmax = 30)
figure1 = gcurve(color = color.red, label = "Grenade") # Grenade curve
figure2 = gcurve(color = color.blue, label = "Piece 1")    # Exploded piece 1
figure3 = gcurve(color = color.yellow, label = "Piece 2")  # Exploded piece 2
figure4 = gcurve(color = color.orange, label = "Center of Mass")  # Center of Mass

# ========================================== Exit button section ========================================== #

wtext(text = "\n")
exit_button = button(bind = sim.exit, text = "Exit simulation", background = color.red, color = color.white)
wtext(text = "\n")

# ========================================== Physical simulation section ========================================== #

# Question: A grenade is thrown with initial velocity v o from the origin at the top of a high
# cliff, subject to negligible air resistance. (a) Using a suitable plotting program, plot the orbit, with
# the following parameters: v. = (4, 4), g = 1, and 0 < t < 4 (and with x measured horizontally and y
# vertically up). Add to your plot suitable marks (dots or crosses, for example) to show the positions
# of the grenade at t = 1, 2, 3, 4. (b) At t = 4, when the grenade's velocity is v, it explodes into two
# equal pieces, one of which moves off with velocity v + ∆v. What is the velocity of the other piece?
# (c) Assuming that ∆v = (1, 3), add to your original plot the paths of the two pieces for 4 < t < 9. Insert
# marks to show their positions at t = 5, 6, 7, 8, 9. Find some way to show clearly that the CM of the two
# pieces continues to follow the original parabolic path.

grenade = sphere(pos = vector(-10, 0, 0), radius = 1, color = color.red, make_trail = True)
grenade.mass = 10
grenade.momentum = grenade.mass * vector(4, 4, 0)
net_mass = grenade.mass

gravity = vector(0, -1, 0)

# ========================================== Animation loop ========================================== #

t = 0
dt = 0.001
exploded = False    # Flag to track when ball explodes

while sim.running:
    rate(1000)
    if t <= 4:
        
        grenade.momentum += (grenade.mass * gravity) * dt
        grenade.pos += (grenade.momentum / grenade.mass) * dt

        figure1.plot(grenade.pos.x, grenade.pos.y)
    
    elif t > 4 and not exploded: 
        piece1 = sphere(pos = grenade.pos, radius = grenade.radius / 2, color = color.blue, make_trail = True)  # Create piece 1
        piece2 = sphere(pos = grenade.pos, radius = grenade.radius / 2, color = color.yellow, make_trail = True)    # Create piece 2

        piece1.mass = grenade.mass / 2
        piece2.mass = grenade.mass / 2

        cm_pos = ((piece1.mass * piece1.pos) + (piece2.mass * piece2.pos)) / net_mass
        cm_tracker = sphere(pos = cm_pos, radius = grenade.radius / 5, color = color.orange, make_trail = True)   # Create a point to show motion of CM

        
        piece1.deltavelocity = vector(1, 3, 0)

        piece1.momentum = piece1.mass * ((grenade.momentum / grenade.mass) + piece1.deltavelocity)  # m'(v + δv)
        piece2.momentum = grenade.momentum - piece1.momentum    # Momentum is conserved since no external force on system
        cm_tracker.momentum = grenade.momentum

        print(piece2.momentum / piece2.mass)    # Prints the velocity of the second piece at ~ 4s; Assuming ∆v = (1, 3)

        exploded = True

    elif t > 4 and t <= 9 and exploded:

        piece1.momentum += (piece1.mass * gravity) * dt
        piece2.momentum += (piece2.mass * gravity) * dt
        cm_tracker.momentum += (net_mass * gravity) * dt

        piece1.pos += (piece1.momentum / piece1.mass) * dt
        piece2.pos += (piece2.momentum / piece2.mass) * dt
        cm_tracker.pos += (cm_tracker.momentum / net_mass) * dt

        figure2.plot(piece1.pos.x, piece1.pos.y)
        figure3.plot(piece2.pos.x, piece2.pos.y)
        figure4.plot(cm_tracker.pos.x, cm_tracker.pos.y)

    t += dt

