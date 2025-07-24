from vpython import *

# This simulation creates a button which when clicked changes the color of a ball

ball = sphere(color = color.cyan)

def changecolor(evt):
    if evt.text == 'red':
        ball.color = color.red
        clrbtn.background = color.cyan
        clrbtn.text = 'cyan'
    else:
        ball.color = color.cyan
        clrbtn.text = 'red'
        clrbtn.background = color.red

clrbtn = button(bind = changecolor, text ='red', background = color.red)

while True:
    rate(100)