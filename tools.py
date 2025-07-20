from vpython import *

# This file contains all useful functions that can be alloted as a bind to various interactable classes in VPython

# Exit bind for button class
class Simulation:
    def __init__(self):
        self.running = True # Creates a running instance

    def exit(self):
        self.running = False
        print("User exit.")
