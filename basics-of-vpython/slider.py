from vpython import *

# This program builds an interactive field allowing the user to vary certain parameters of the box

running = True  # Define running flag to handle exit button
scene.caption
theta = 0
b = box(pos = vector(0, 0, 0), size = vector(0.5, 0.2, 0.2), color = color.red)
#velocity = vector(0, 0, 0)

def exit():
    global running
    running = False
    print("User exit.")

button(bind = exit, text = "Exit simulation", background = color.red, color = color.white)
wtext(text = "\n\n")

def slider_func(evt):
    global theta
    if evt.id == 'x':
        b.size.x = evt.value
        x_wtext.text = f"Length of box is {evt.value}m"

    elif evt.id == 'y':
        b.size.y = evt.value
        y_wtext.text = f"Height of box is {evt.value}m"

    elif evt.id == 'angle':
        theta = evt.value
        b.axis = b.size.x * vector(cos(theta), sin(theta), 0)   # Axis vector by default handles sets/handles length (box.size.x) to 1
        angle_wtext.text = f"Angular position of box is {(evt.value) * (180 / pi):.2f} degrees"
    
# ========================================== Sliders and labels ========================================== #

wtext(text = "Length of box")
xslider = slider(bind = slider_func, max = 2, min = 0.5, step = 0.01, value = b.size.x, id = 'x')
x_wtext = wtext(text = "Length of box is 0.5m")
wtext(text = "\n\n")

wtext(text = "Width of box")
yslider = slider(bind = slider_func, max = 2, min = 0.2, step = 0.01, value = b.size.y, id = 'y')
y_wtext = wtext(text = "Height of box is 0.5m")
wtext(text = "\n\n")

wtext(text = "Angle of the box")
angleslider = slider(bind = slider_func, max = 2*pi, min = 0, step = pi / 180, value = theta, id = 'angle')
angle_wtext = wtext(text = "Angular position of box is 0 degrees")
wtext(text = "\n\n")

dt = 0.01

# ========================================== Animation loop ========================================== #

while running:
    rate(100)

    #b.pos += velocity * dt # Animation of box moving
