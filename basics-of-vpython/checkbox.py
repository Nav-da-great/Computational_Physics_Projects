from vpython import *
from tools import *

# A checkbox in VPython has two states: Selected and not selected
# This simulation creates a checkbox bind (rotate) that toggles the spin attribute of a cube

canvas(width = 1900, height = 600, background = color.black, title = "<h1>Checkbox demonstration</h1>")

cube = box(color = color.magenta)
spin = True
sim = Simulation()

def rotate(evt):
    global spin

    if evt.checked:
        spin = True
        
    else:
        spin = False

wtext(text = "\n" + " " * 177)
check = checkbox(bind = rotate, text = "Toggle spin", checked = True)   # Checkbox
wtext(text = "\n" + " " * 177)
exit_button = button(bind = sim.exit, text = "Exit simulation", background = color.red, color = color.white)    # Exit button

while sim.running:
    rate(100)

    if spin:
        cube.rotate(angle = pi / 200, axis = vector(0, 1, 0))