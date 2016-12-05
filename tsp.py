from search import * 

class TspState(StateSpace):
    def __init__(self, actin, gval, parent):
        StateSpace.__init__(self, action, gval, parent)
    
    def successors(self):
        pass

    def hashable_state(self):
        pass
    
    def state_string(self):
        pass
    
    def print_state(self):
        pass

def tsp_goal_state(state):
    pass