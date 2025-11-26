# Repository Structure

This document provides a breakdown of all files and directories in this repository apart from [README.md](README.md), [DEMO.md](DEMO.md), [WHY.md](WHY.md), and other standard files.

| File/Folder | Description |
|-------------|-------------|
| [**/basic_computational_methods**](/basic_computational_methods) | Contains Python implementation of the most basic and common numerical methods |
| [differentiators.py](basic_computational_methods/differentiators.py) | Defines simple, three-point and five-point numerical derivative functions |
| [integrators.py](basic_computational_methods/integrators.py) | Defines simple and trapezoidal numerical integration functions |
| [rootfinders.md](basic_computational_methods/root_finders.md) | Contains basic explanations of some common root finding methods |
| [rootfinders.py](basic_computational_methods/root_finding_tools.py) | Defines bisection, Newton-Raphson and secant root finding methods |
| [**/classical_mechanics**](/classical_mechanics) | Contains Python scripts that simulate phenomenon explained via Classical Mechanics |
| [angular_momentum.py](classical_mechanics/angular_momentum.py) | Visualizes angular momentum of a binary star system |
| [double_pendulum.py](classical_mechanics/double_pendulum.py) | Simulation of a double pendulum to visualize classical chaos; uses spring forces (very high stiffness) to avoid defining constraints for tension in the pendulums |
| [interactive_pendulum.py](classical_mechanics/interactive_pendulum.py) | Simulates a pendulum whose initial position — among other things — can be varied by clicking and dragging the bob |
| [orbits.py](classical_mechanics/orbits.py) | Visualizes the orbit of an artificial satellite around the Earth and plots various energy curves |
| [pi_from_blocks.py](classical_mechanics/pi_from_blocks.py) | Rough calculation of the digits of pi via elastic collisions between two blocks. Incredibly well-known because of 3blue1brown's videos. [This](https://www.youtube.com/watch?v=HEfHFsfGXjs) and [this](https://www.youtube.com/watch?v=6dTyOl1fmDo)|
| [projectile_motion_with_drag.py](classical_mechanics/projectile_motion_with_drag.py) | Simulation of the motion of a projectile launched at an angle under the influence of gravity without and with drag forces acting on it |
| [**/electromagnetism**](/electromagnetism) | Contains Python scripts that simulate phenomenon explained via Electromagnetic Theory |
| [electric_field.py](electromagnetism/electric_field.py) | Visualizes the changing electric field by virtue of motion between moving charged particles |
| [**/misc**](/misc) | Contains scripts that I couldn't fit into a particular category |
| [potential_field_path_finding_method.py](misc/potential_field_path_finding_method.py) | Implementation of a classic path finding algorithm (in robotics) based on potential fields |
| [**/statistical_mechanics**](/statistical_mechanics) | Contains Python scripts that simulate phenomenon explained via Statistical Mechanics |
| [brownian_motion.py](statistical_mechanics/brownian_motion.py) | Simulation of brownian motion of a large particle |
| [**/taylor_computer_solutions**]() | Solutions to selected computer-based problems from Classical Mechanics by John R. Taylor (2005) |
| [problem-2-55.py](taylor-computer-solutions/problem-2-55.py) | [_NOT A COMPUTER-BASED PROBLEM_] Plotting the helical motion of a charged particle under a crossed electric and magnetic field |
| [problem-3-23.py](taylor-computer-solutions/problem-3-23.py) | Solution to problem 3.23 (Context of the problem is in the file) |
| [**/utilities**](/utilities) | Contains ```tools.py``` |
| [tools.py](utilities/tools.py) | Contains the Simulation utility class, which provides basic GUI controls for VPython-based simulations. These include the ```exit_bind``` and ```pause_bind``` methods |
