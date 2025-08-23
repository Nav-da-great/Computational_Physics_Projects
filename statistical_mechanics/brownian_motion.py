from vpython import *
from utilities.tools import Simulation

sim = Simulation()
canvas(width = 1900, height = 600)
# ========================================== Pause button section ========================================== #
wtext(text = "\n\n" + " " * 183)
pause_button = button(bind = sim.pause_bind, text = "Play", background = color.green, color = color.white)

# ========================================== Exit button section ========================================== #

wtext(text = "\n\n" + " " * 177)
exit_button = button(bind = sim.exit_bind, text = "Exit simulation", background = color.red, color = color.white)

# ========================================== Physical simulation section ========================================== #

# Initializations
k = 2000
k_temp = 1
particles = []
particles_mass = 0.1
particle_radius = 0.01

big_particle_mass = 1000
big_particle_radius = particle_radius * 5

wall_thickness = 1 / 20

# Create big particle
big_particle = sphere(pos = vector(0, 0, 0), radius = big_particle_radius, color = color.cyan, make_trail = True)
big_particle.momentum = vector(0, 0, 0)

def system_creator(l = 1, h = 1, w = 1, thick = 1 / 20, n = 10):
    global bottom, top, left, right, back
    # Create system skeleton
    bottom = box(pos = vector(0, -h / 2, 0), length = l, height = thick, width = w)
    top = box(pos = vector(0, h / 2, 0), length = l, height = thick, width = w)
    left = box(pos = vector(-l / 2, 0, 0), length = thick, height = h, width = w)
    right = box(pos = vector(l / 2, 0, 0), length = thick, height = h, width = w)
    back = box(pos = vector(0, 0, -w / 2), length = l, height = h, width = thick)

    # Populate with particles
    temp_particles = []
    temp_particles.append(big_particle)
    for i in range(n):
        while True:
            position = vector((l/2 - thick) * (1 - 2*random()), (h/2 - thick) * (1 - 2*random()), 0)
            overlap = False
            for p in temp_particles:
                if (mag(p.pos - position) < 1.2*(p.radius + particle_radius)):
                    overlap = True
                    break
            if not overlap:
                break
        temp = sphere(pos = position, radius = particle_radius, color = color.orange)
        particles.append(temp)
        temp_particles.append(temp)
        particles[i].momentum = particles_mass * vector(random(), random(), 0) 
        
system_creator(1/2, 1/2, 0.125, wall_thickness, 50)

# ========================================== Animation loop ========================================== #
dt = 0.001
while sim.running:
    rate(700)

    if not sim.pause:

        if (big_particle.pos.x + big_particle_radius/2 > right.pos.x - wall_thickness):
            force = 0.1 * k * vector(-1, 0, 0)
            big_particle.momentum += force * dt
        if (big_particle.pos.x - big_particle_radius/2 < left.pos.x + wall_thickness):
            force = 0.1 * k * vector(1, 0, 0)
            big_particle.momentum += force * dt
        if (big_particle.pos.y + big_particle_radius/2 > top.pos.y - wall_thickness):
            force = 0.1 * k * vector(0, -1, 0)
            big_particle.momentum += force * dt
        if (big_particle.pos.y - big_particle_radius/2 < bottom.pos.y + wall_thickness):
            force = 0.1 * k * vector(0, 1, 0)
            big_particle.momentum += force * dt
        
        for i in range(len(particles)):
            # Wall-particle collisions
            
            if (particles[i].pos.x + particle_radius/2 > right.pos.x - wall_thickness):
                force = 0.01 * k * vector(-1, 0, 0)
                particles[i].momentum += force * dt
            if (particles[i].pos.x - particle_radius/2 < left.pos.x + wall_thickness):
                force = 0.01 * k * vector(1, 0, 0)
                particles[i].momentum += force * dt
            if (particles[i].pos.y + particle_radius/2 > top.pos.y - wall_thickness):
                force = 0.01 * k * vector(0, -1 ,0)
                particles[i].momentum += force * dt
            if (particles[i].pos.y - particle_radius/2 < bottom.pos.y + wall_thickness):
                force = 0.01 * k * vector(0, 1, 0)
                particles[i].momentum += force * dt
            
            # particle-particle collisions
            for j in range(i + 1, len(particles)):
                L1 = particles[j].pos - particles[i].pos
                if not (mag(L1) > 2*1.2* particle_radius):
                    force_ij = k * (mag(L1) - 2*1.2*particle_radius) * norm(L1)
                    force_ji = -force_ij

                    particles[i].momentum += force_ij * dt
                    particles[j].momentum += force_ji * dt
        
        # big particle-particle collisions
        for i in range(len(particles)):
            L2 = big_particle.pos - particles[i].pos
            if not (mag(L2) > big_particle.radius + particle_radius):
                force_bp = 10 * k * (mag(L2) - (big_particle.radius + particle_radius)) * norm(L2)
                force_pb = -force_bp

                big_particle.momentum += force_pb * dt
                particles[i].momentum += force_bp *dt
        
            particles[i].pos += (particles[i].momentum / particles_mass) * dt
            big_particle.pos += (big_particle.momentum / big_particle_mass) * dt
