from vpython import *

# This file contains all useful functions that can be used as a bind to various interactable classes in VPython

class Simulation:
    def __init__(self):
        self.running = True # Creates a running instance
        self.pause = True

    # Exit bind
    def exit_bind(self):
        self.running = False
        print("User exit.")
    
    # Pause bind
    def pause_bind(self, evt):
        self.pause = not self.pause
        if evt.text == "Pause": 
            evt.text = "Play"
            evt.background = color.green
        else: 
            evt.text = "Pause"
            evt.background = color.blue
