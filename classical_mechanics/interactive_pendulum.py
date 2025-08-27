from vpython import *
from utilities.tools import Simulation

sim = Simulation()

exit_button = button(bind = sim.exit_bind, text = "Exit", background = color.red, color = color.white)
wtext(text = "\n")
pause_button = button(bind = sim.pause_bind, text = "Pause", background = color.blue, color = color.white)

drag = False

def pos_setter(evt):
    global drag
    if evt.event == "mousedown":
        drag = True
    if evt.event == "mouseup":
        drag = False

scene.bind("mousedown mouseup", pos_setter)

l1 = 5
θ1 = 0 * (pi / 180)
w1 = 0
a1 = 0
bob1 = sphere(pos = l1 * vector(sin(θ1), -cos(θ1), 0), color = color.red, make_trail = False, retain = 100)
bob1.mass = 1
bob1.momentum = bob1.mass * vector(0,0,0)
rod1 = cylinder(pos = vector(0,0,0), axis = bob1.pos, radius = 0.1)

def binds(evt):
    global l1
    if evt.id == 'l':
        l1 = evt.value
    if evt.id == 't':
        bob1.make_trail = not (bob1.make_trail)
        if bob1.make_trail:
            evt.text = "Trail off"
            evt.background = color.yellow
        else:
            evt.text = "Trail on"
            evt.background = color.magenta
            bob1.clear_trail()

wtext(text = "\n\n")
length_slider = slider(bind = binds, max = 20, min = 5, step = 0.01, id = 'l')
wtext(text = "\n\n")
trail_toggle = button(bind = binds, text = "Trail on", background = color.magenta, id = 't')

gravity = 9.8
dt = 0.01
while sim.running:
    rate(100)
    if not sim.pause:
        # Handling positions upon mousedown within range of a bob
        if (mag(bob1.pos - scene.mouse.pos) < 2 * bob1.radius):
            while drag:
                θ_temp = atan2(scene.mouse.pos.x, -scene.mouse.pos.y)
                bob1.pos = l1 * vector(sin(θ_temp), -cos(θ_temp), 0)
                θ1 = θ_temp
                a1 = 0
                w1 = 0
                rod1.axis = bob1.pos
        a1 = (-gravity/l1) * sin(θ1)
        w1 += a1 * dt
        θ1 += w1 * dt
        bob1.pos = l1 * vector(sin(θ1), -cos(θ1), 0)
        rod1.axis = bob1.pos