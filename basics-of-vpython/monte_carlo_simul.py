from vpython import *

# Calculating the value of pi using a monte-carlo simulation (circle)

g = graph(width = 800, height = 800)
f_in = gdots(color = color.red)
f_out = gdots(color = color.blue)

total_dots = 10000
count = 0
number_of_points_inside = 0

while True:
    if count <= total_dots:
        rate(5000)
        r = vector(random(), random(), 0)
        if mag(r) < 1:
            number_of_points_inside += 1
            f_in.plot(r.x, r.y)
        else:
            f_out.plot(r.x, r.y)

        count += 1
