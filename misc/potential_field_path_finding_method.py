from vpython import *
import random

scene = canvas(title = "<b>Potential Field method for obstacle avoidance</b>", width = 1000, height = 500)
# ========================================== GUI ========================================== #
class Simulation:
    def __init__(self):
        self.running = True
        self.pause = True

    def exit_bind(self):
        self.running = False
        print("User exit.")
    
    def pause_bind(self, evt):
        self.pause = not self.pause
        if evt.text == "Pause": 
            evt.text = "Play"
            evt.background = color.green
        else: 
            evt.text = "Pause"
            evt.background = color.blue
    def reset_bind(self):
    
        global robot, goal, obstacles

        # Reset all positions
        robot.pos = vector(x_start, base_y, 0)
        robot.make_trail = False
        robot.clear_trail()

        goal.pos = vector(x_start + spacing, base_y, 0)

        obs_positions = [
            x_start + 2*spacing,
            x_start + 3.2*spacing,
            x_start + 4.4*spacing,
            x_start + 5.6*spacing
        ]
        for i, obs in enumerate(obstacles):
            obs.pos = vector(obs_positions[i], base_y, 0)

        # Pause simulation
        self.pause = True
        pause_button.text = "Play"
        pause_button.background = color.green
        print("Simulation reset.")


sim = Simulation()
scene.append_to_caption("\nDrag objects to desired positions, then press 'Play' to start simulation.\n")

# Buttons
exit_button = button(bind=sim.exit_bind, text="Exit simulation", background=color.red, color=color.white)
wtext(text = "\n")
pause_button = button(bind=sim.pause_bind, text="Play", background=color.green, color=color.white)
wtext(text = "\n")
wtext(text = "Press 'reset' to revert to initial positions")
wtext(text = "\n")
reset_button = button(bind=sim.reset_bind, text="Reset", background=color.orange, color=color.white)

# ========================================== Initialization ========================================== #

zeta = 0.2
r_a = 0.8
eta = 0.2
d0 = 0.5
k_tan = 0.02
h = 0.08
eps = 1e-6

# Layout setup (top-left corner)
base_y = 5
x_start = -10
spacing = 2

robot = sphere(pos=vector(x_start, base_y, 0), radius=0.5, color=color.blue, make_trail=False)
goal  = sphere(pos=vector(x_start + spacing, base_y, 0), radius=0.3, color=color.green)

obstacles = [
    cylinder(pos=vector(x_start + 2*spacing, base_y, 0), axis=vector(0, 0, 2), radius=0.7, color=color.red),
    cylinder(pos=vector(x_start + 3.2*spacing, base_y, 0), axis=vector(0, 0, 2), radius=0.7, color=color.red),
    cylinder(pos=vector(x_start + 4.4*spacing, base_y, 0), axis=vector(0, 0, 2), radius=0.7, color=color.red),
    cylinder(pos=vector(x_start + 5.6*spacing, base_y, 0), axis=vector(0, 0, 2), radius=0.7, color=color.red)
]

# ========================================== Utility functions ========================================== #

def to_xy(v):
    return vector(v.x, v.y, 0)

def attractive_force(pos):
    p = to_xy(pos)
    pg = to_xy(goal.pos)
    diff = p - pg
    d_g = mag(diff)
    if d_g < eps:
        return vector(0, 0, 0)
    if d_g <= r_a:
        return -zeta * diff
    else:
        return -zeta * r_a * (diff / d_g)

def repulsive_and_tangential_forces(pos):
    p = to_xy(pos)
    F_rep_total = vector(0, 0, 0)
    F_tan_total = vector(0, 0, 0)

    for obs in obstacles:
        obs_xy = to_xy(obs.pos)
        goal_vec = to_xy(goal.pos - obs.pos)
        vec_r = p - obs_xy
        dist_center = mag(vec_r)
        d = dist_center - obs.radius - robot.radius

        unit_r = vector(1, 0, 0) if dist_center < eps else vec_r / dist_center
        sign = 1 if dot(cross(unit_r, goal_vec), vector(0,0,1)) > 0 else -1

        if d < 0:
            push_strength = eta * 100
            F_rep = push_strength * (-unit_r) * (-d + 0.1)
            t_hat = sign * vector(-unit_r.y, unit_r.x, 0)
            F_tan = 0.02 * t_hat
        elif d < d0:
            s = (d0 - d) / d0
            F_rep = (eta * s / d0) * unit_r
            t_hat = sign * vector(-unit_r.y, unit_r.x, 0)
            F_tan = k_tan * s * t_hat
        else:
            F_rep = F_tan = vector(0, 0, 0)

        F_rep_total += F_rep
        F_tan_total += F_tan

    return F_rep_total, F_tan_total

# ========================================== Mouse interaction ========================================== #

drag_target = None

def get_mouse_pos_on_xy_plane(event):
    ray = scene.mouse.ray
    proj = scene.mouse.pos
    if abs(ray.z) < 1e-6:
        return vector(proj.x, proj.y, 0)
    t = -proj.z / ray.z
    hit = proj + t * ray
    return vector(hit.x, hit.y, 0)

def on_mouse_down(event):
    global drag_target
    if not sim.pause:
        return
    mpos = get_mouse_pos_on_xy_plane(event)
    # check robot
    if mag(mpos - to_xy(robot.pos)) < robot.radius:
        drag_target = robot
        return
    # check goal
    if mag(mpos - to_xy(goal.pos)) < goal.radius:
        drag_target = goal
        return
    # check obstacles
    for obs in obstacles:
        if mag(mpos - to_xy(obs.pos)) < obs.radius:
            drag_target = obs
            return

def on_mouse_move(event):
    if not sim.pause or drag_target is None:
        return
    mpos = get_mouse_pos_on_xy_plane(event)
    drag_target.pos = vector(mpos.x, mpos.y, drag_target.pos.z)

def on_mouse_up(event):
    global drag_target
    drag_target = None

scene.bind('mousedown', on_mouse_down)
scene.bind('mousemove', on_mouse_move)
scene.bind('mouseup', on_mouse_up)

# ========================================== Simulation loop ========================================== #

while sim.running:
    rate(50)
    if not sim.pause and mag(to_xy(robot.pos) - to_xy(goal.pos)) > eps:
        if not robot.make_trail:
            robot.make_trail = True
        F_att = attractive_force(robot.pos)
        F_rep, F_tan = repulsive_and_tangential_forces(robot.pos)
        F_net = F_att + F_rep + F_tan

        if mag(F_net) > 0.01:
            direction = norm(F_net)
            new_xy = to_xy(robot.pos) + h * direction
            robot.pos = vector(new_xy.x, new_xy.y, robot.pos.z)
        else:
            robot.pos += vector((random.random()-0.5)*1e-4,
                                (random.random()-0.5)*1e-4, 0)
