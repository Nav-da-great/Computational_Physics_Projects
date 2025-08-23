from vpython import *
from utilities.tools import Simulation

# Simulation of projectile motion with and without drag
canvas(width = 1900, height = 800, title = "Simulation of projectile motion with and without drag", background = color.black)
sim = Simulation()
# ========================================== Exit button section ========================================== #

wtext(text = "\n" + " " * 177)
exit_button = button(bind = sim.exit, text = "Exit simulation", background = color.red, color = color.white)

# ========================================== Physical simulation section ========================================== #

# Intializations
u0 = 7.2 # Intial velocity
ball_radius = 0.05
theta = radians(73) # Angle of launch
density = 1.2 # Density of the medium
A = pi*ball_radius**2 # Cross-sectional area of a ball
drag_constant = 0.47 # For a sphere


ball_ideal = sphere(pos = vector(0,0.55,0), radius = ball_radius, color = color.yellow, make_trail = True)
ball_real = sphere(pos = vector(0,0.55,0), radius = ball_radius, color = color.blue, make_trail = True)

ball_ideal.mass = 0.05
ball_real.mass = 0.02

velocity_function = u0*vector(cos(theta), sin(theta), 0)
ball_ideal.momentum = ball_ideal.mass*velocity_function 
ball_real.momentum = ball_real.mass*velocity_function

gravity = vector(0, -9.8, 0)

ground = box(pos = vector(0,0.5,0), size = vector(10, 0.1, 5), color = vector(0.588, 0.294, 0)) # Creates a box

vscale = 0.25
varrow_ideal = arrow(pos = ball_ideal.pos, axis = vscale*(ball_ideal.momentum/ball_ideal.mass), color = color.red) # Creates an arrow
varrow_real = arrow(pos = ball_ideal.pos, axis = vscale*(ball_real.momentum/ball_real.mass), color = color.red)

#curve1 = gcurve(color = color.blue)

# ========================================== Animation loop ========================================== #

t = 0
dt = 0.0001
while sim.running:
    rate(3000)
    if ball_ideal.pos.y >= ball_ideal.radius + ground.pos.y:
        
        drag_force = -(1/2)*density*A*drag_constant*(mag(ball_real.momentum)**2/ball_real.mass**2)*norm(ball_real.momentum)

        ball_ideal.momentum += (ball_ideal.mass*gravity) * dt
        ball_real.momentum += (ball_real.mass*gravity + drag_force) * dt

        ball_ideal.pos += (ball_ideal.momentum/ball_ideal.mass) * dt
        ball_real.pos += (ball_real.momentum/ball_real.mass) * dt

        varrow_ideal.pos = ball_ideal.pos
        varrow_ideal.axis = vscale * (ball_ideal.momentum/ball_ideal.mass)
        varrow_real.pos = ball_real.pos
        varrow_real.axis = vscale * (ball_real.momentum/ball_real.mass)

        t += dt

