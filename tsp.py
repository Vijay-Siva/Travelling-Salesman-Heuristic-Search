from search import *

'''
    A) Class TSP

    A specialization of the StateSpace Class that is tailored to the travelling 
    salesman problem.

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
        current_vertex = self.get_current_vertex()

        #loop through edges that contain the current vertex, and an untouched vertex
        for edge in self.get_edges(current_vertex):

            # get the untouched vertex
            tail = edge[1]
            if (edge[1] == current_vertex):
                tail = edge[0]

            #create and add the state 
            state = TSPState(self.state_string() + str(edge) + " ", self.gval + edge[2], self, self.path_vertices + [tail], 
                        [x for x in self.unexplored_vertices if x != tail], 
                        self.path_edges + [edge], [x for x in self.unexplored_edges if x != edge], self.optimal_weight)
            successors.append(state)

        return successors

    def hashable_state(self):
        '''
        Return a data item that can be used as a dictionary key to UNIQUELY represent a state.
        '''
        return hash(tuple(self.path_edges)); 

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
        Prints the string representation of the state. 
        '''    
        print(self.state_string())

    def get_edges(self, vertex):
        '''
        Return all the outgoing untouched edges for the given vertex in self.
        @param vertex
        @return list of edges 
        '''
        result = []
        for edge in self.unexplored_edges:
            tail = edge[1]
            if (edge[1] == vertex):
                tail = edge[0]

            if (vertex in edge[0:2] and tail not in self.path_vertices):
                result.append(edge)

        return result

    def get_all_edges(self, vertex):
        '''
        Return all the outgoing edges for the given vertex in self.
        @param vertex
        @return list of edges 
        '''
        return [e for e in self.unexplored_edges + self.path_edges if vertex in e[0:2]]

    def get_current_vertex(self):
        ''' Get the current vertex in the path'''
        if len(self.path_vertices) > 0:
            return self.path_vertices[-1]
        return 1

def goal_state(state):
    '''
    Returns True iff the path_edges in the given TSPState form a Hamiltonian cycle 
    with minimum weight. 
    @param TSPState: The state that we want to check 
    '''
    return (sum([x[2] for x in state.path_edges]) == state.optimal_weight and 
                len(state.path_edges) == state.order)
