from vpython import *

lol = graph(title = "Angular momentum of planet", xtitle = "time", ytitle = "Angular momentum", ymin = 0)
figure1 = gcurve(color = color.blue)
figure2 = gcurve(color = color.yellow)
figure3 = gcurve(color = color.red)

G = 6.67e-11
v_earth = 3e4

earth_to_sun = 1.5e11
sun = sphere(pos = vector(0, 0, 0), radius = earth_to_sun / 10, color = color.yellow, make_trail = True)
sun.mass = 2e30

planet = sphere(pos = vector(earth_to_sun, 0, 0), radius = earth_to_sun / 20, color = color.blue, make_trail = True)
planet.mass = 6e29

planet.momentum = planet.mass * vector(0, v_earth, 0)
sun.momentum = -planet.momentum

v_arrow_scale = 1.5 * 10e5
planet_velocity_arrow = arrow(pos = planet.pos, axis = v_arrow_scale * (planet.momentum / planet.mass), color = planet.color)
sun_velocity_arrow = arrow(pos = sun.pos, axis = v_arrow_scale * (sun.momentum / sun.mass), color = sun.color)

a_arrow_scale = 1.5 * 10e-6
planet_amomentum_arrow = arrow(pos = planet.pos, color = color.magenta)
sun_amomentum_arrow = arrow(pos = sun.pos, color = color.orange)

t = 0
dt = 10000


while True:
    rate(100)

    r = sun.pos - planet.pos
    F_gravity = (G * sun.mass * planet.mass * norm(r)) / mag2(r)

    sun.momentum -= F_gravity * dt
    sun.pos += (sun.momentum / sun.mass) *dt
    sun_velocity_arrow.pos = sun.pos
    sun_velocity_arrow.axis = 5 * v_arrow_scale * (sun.momentum / sun.mass)

    planet.momentum += F_gravity * dt
    planet.pos += (planet.momentum / planet.mass) * dt
    planet_velocity_arrow.pos = planet.pos
    planet_velocity_arrow.axis = v_arrow_scale * (planet.momentum / planet.mass)

    angular_momentum_planet = cross(planet.pos, planet.momentum)
    planet_amomentum_arrow.pos = planet.pos
    planet_amomentum_arrow.axis = a_arrow_scale * (angular_momentum_planet / planet.mass)

    angular_momentum_sun = cross(sun.pos, sun.momentum)
    sun_amomentum_arrow.pos = sun.pos
    sun_amomentum_arrow.axis = 10 * a_arrow_scale * (angular_momentum_sun / sun.mass)
    
    
    figure1.plot(t, mag(angular_momentum_planet))
    figure2.plot(t, mag(angular_momentum_sun))
    figure3.plot(t, mag(angular_momentum_planet + angular_momentum_sun))

    t += dt


