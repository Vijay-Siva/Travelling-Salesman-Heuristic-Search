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
        if path_vertices == []:
            self.path_vertices = [unexplored_vertices.pop(0)]
        else:
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
        for edge in self.get_edges(self.get_current_vertex()):
            state = TSPState(self.state_string() + str(edge) + " ", edge[2], self, self.path_vertices + [edge[1]], 
                        [x for x in self.unexplored_vertices if x != edge[1]], 
                        self.path_edges + [edge], [x for x in self.unexplored_edges if x != edge], self.optimal_weight)
            successors.append(state)

        return successors

    def hashable_state(self):
        '''
        Return a data item that can be used as a dictionary key to UNIQUELY represent a state.
        '''
        return hash(sum([x[2] for x in self.path_edges]))

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
        return [e for e in self.unexplored_edges if vertex in e[0:2] and e[1] not in self.path_vertices]

    def get_all_edges(self, vertex):
        '''
        Return all the outgoing edges for the given vertex in self.
        '''
        return [e for e in self.unexplored_edges + self.path_edges if vertex in e[0:2]]

    def get_current_vertex(self):
        ''' Get the current vertex in the path'''
        if len(self.path_vertices) > 0:
            return self.path_vertices[-1]
        return 1

def goal_state(state):
    '''
    Returns True iff the given TSP state is a goal state. 
    @param TSPState: The state that we want to check 
    '''
    return state.unexplored_vertices == []
    #(sum([x[2] for x in state.path_edges]) == state.optimal_weight and 
    #            len(state.path_edges) == state.order)
