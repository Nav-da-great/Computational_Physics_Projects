from vpython import *

g = graph(title = "Constant acceleration", xtitle = "time", ytitle = "Distance travelled",
          width = 800, height = 500) #Controls aspects about the window
figure1 = gcurve(color = color.blue) #Creates a curve between the given points
figure2 = gcurve(color = color.red)
x_a = 0.5
x_b = 0
v_a = 0.45
v_b = 0
a_b = 0.2
t = 0
dt = 0.01 #Time interval

while True:
    rate(100)
    while t < 8:
        x_a += v_a*dt
        x_b += v_b*dt
        
        v_b += a_b*dt

        t += dt

        figure1.plot(t,x_a)
        figure2.plot(t,x_b)
