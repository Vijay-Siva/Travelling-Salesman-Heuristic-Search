
from search import *


class TSP():

   def __init__(self, vertices, edges, path=[]):
       self.order = len(vertices) 
       self.vertices = vertices 
       self.edges = edges
       self.path = path

'''
    A) Class TSP

    A specialization of the StateSpace Class that is tailored to the travelling 
    salesman problem

'''
from search import * 
class TSP(StateSpace):
    def __init__(self, action, gval, parent, vertices, edges, path, goal):
        '''
        Creates a new TSP state 
        @param vertices: The set of vertices the graph contains
        @param edges: The set of edges the graph has, of the form (v1, v2, weight)
        @param path: The path so far in the search for a minimum hamiltonian cycle
        @param goal: The optimal hamiltonian cycle for this TSP formulation
        '''
        StateSpace.__init__(self, action, gval, parent)
        self.order = len(vertices) 
        self.vertices = vertices 
        self.edges = edges
        self.path = path
        self.goal = goal 
        return
    
    def successors(self):
        '''
        Generates all the actions that can be performed from this state, and the states those actions will create.
        '''
        successors = [] 
        visited = Set()
        for edges in self.path:
            visited.add(edge[0])
        
        visited.add(self.path[-1][1])

        unvisited = [x for x in self.vertices and x not in visited]

        for vertex in visited:
            for edge in self.get_edges(vertex):
                if (edge[1] in unvisited):
                    new_state = TSP(str(edge), self.gval + edge[2], self, self.vertices, self.edges, path + [edge], this.goal)
                    successors.append(new_state)

        return successors 

    def hashable_state(self):
        '''Return a data item that can be used as a dictionary key to UNIQUELY represent a state.'''
        return hash((self.vertices, self.edges, self.path))

    def state_string(self):
        '''Returns a string representation fo a state that can be printed to stdout.''' 
        s = "" 
        for x in self.path:
            s += str(x) + ", "
        
        return s
 
    def print_state(self):
        '''
        Prints the string representation of the state. ASCII art FTW!
        '''    
        print("ACTION was " + self.action)
        print(self.state_string())

    def get_edges(self, vertex):
        '''Return all the outgoing edges for the given vertex in self.'''
        result = []
        for edge in self.edges:
            if (edge[0] == vertex):
                result.append(edge)
        return result

    def get_current_vertex(self):
        ''' Get the current vertex in the path'''
        if len(path) > 0:
            return path[-1][1]
        else:
            return None

'''
TSP Problem Set, for testing TODO 
'''