from search import *


'''
    A) Class TSP

    A specialization of the StateSpace Class that is tailored to the travelling 
    salesman problem

'''
from search import * 

class TSPState(StateSpace):
    def __init__(self, action, gval, parent, path_vertices, unexplored_vertices,
                 path_edges, unexplored_edges, optimal_weight):
        '''
        Creates a new TSP state 
        @param path_vertices: The set of vertices visited so far 
        @param unexplored_vertices: The set of vertices not visited yet 
        @param path_edges: Edges travelled through so far
        @param unexplored_edges: Edges we have not travelled through yet
        @param optimal_weight: The weight of the optimal path in the graph 
        '''
        StateSpace.__init__(self, action, gval, parent)
        self.order = len(path_vertices) + len(unexplored_vertices)

        # vertices in graph =  path_vertices + unexplored_vertices, and likewise
        # for edges, in the interest of time complexity (at expense of space complexity)
        self.path_vertices = path_vertices
        self.unexplored_vertices = unexplored_vertices
        self.path_edges = path_edges
        self.unexplored_edges = unexplored_edges
        self.optimal_weight = optimal_weight
    
    def successors(self):
        '''
        Generates the list of states that can be reached from the current state.
        '''
        successors = []
        for e in self.get_edges(self, self.get_current_vertex):
            if e[0] == self.get_current_vertex:
                w = e[1]
            else:
                w = e[0]
            self.unexplored_vertices.remove(w)
            self.unexplored_edges.removes(w)
            successors.append(TSPState(self.action, self.gval + e.weight, 
                self.get_current_vertex, self.path_vertices + [w], 
                self.unexplored_vertices, self.path_edges + [e]))
        
        return successors 

    def hashable_state(self):
        '''
        Return a data item that can be used as a dictionary key to UNIQUELY represent a state.
        '''
        return hash(self.path_edges)

    def state_string(self):
        '''
        Returns a string representation fo a state that can be printed to stdout.
        ''' 
        s = "" 
        for e in self.path_edges:
            s += str(e) + "  "
        return s
 
    def print_state(self):
        '''
        Prints the string representation of the state. ASCII art FTW!
        '''    
        print(self.state_string())

    def get_edges(self, vertex):
        '''
        Return all the outgoing untouched edges for the given vertex in self.
        '''
        return [e for e in self.unexplored_edges if vertex in e[0:2]]

    def get_all_edges(self, vertex):
        '''
        Return all the outgoing edges for the given vertex in self.
        '''
        return [e for e in self.unexplored_edges + self.path_edges if vertex in e[0:2]]

    def get_current_vertex(self):
        ''' Get the current vertex in the path'''
        return self.path_vertices[-1]

def goal_state(TSPState):
    '''
    Returns True iff the given TSP state is a goal state. 
    @param TSPState: The state that we want to check 
    '''
    sum = 0
    for edge in self.path:
        sum += edge[2]
    
    return sum == self.optimal_weight 

#TSP test cases 

Problems = (
    TSPState("Start", 0, None, [], [1, 2, 3, 4], [], 
            [(1, 2, 1), (2, 3, 1), (3, 2, 1), (4, 1, 1), (2, 4, 5), (1, 3, 7)], 4)
)