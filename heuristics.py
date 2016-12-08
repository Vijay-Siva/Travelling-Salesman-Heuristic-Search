from random import random
from math import ceil
import sys


def rand(state):
    '''
    Heuristic 1: Random
    
    Returns a value between 1 - # unexplored verticies in the graph.

    Since the min weight of an edge is 1, this will always return a distance
    less than or equal to the actual distance to goal.
    '''
    return ceil(len(state.unexplored_vertices)*random())

def two_shortest(state):
    '''
    Heuristic 2: Two Shortest
    
    Computes the total weight of the stortest edge connected to first element on 
    the path (to which the traveller must eventually return), and the shortest edge 
    connected to the last (current) element on path.

    Since this heuristic "looks forward" to two two verticies on the path, and finds the 
    shortest edge connected to those two verticies, this will always return a
    distance less than or equal to the actual distance to goal. In the case that the current state
    is the first vertex or last before returning to start in the problem, it will only return the
    shortest weight connected to that vertex.
    '''

    # if first or last vertex, only examine that one
    if state.path_vertices == [] or state.unexplored_vertices == []:
        return state.get_min_edge_weight(state.get_current_vertex)
    
    else:
        return state.get_min_edge_weight(state.path_vertices[0])
        + state.get_min_edge_weight(state.path_vertices[-1])

def greedy(state):
    '''
    Heuristic 3: Greedy 
    
    Calculates how far the current vertex is from it's nearest untouched neighbour

    The optimal path containing this current vertex must trivially include
    this vertex's shortest connected edge.

    '''
    return state.get_min_edge_weight(state.get_current_vertex())

def mst(state):
    '''
    Heuristic 4: Minimum Spanning Tree
    
    Computes the minimum spanning tree of the untouched verticies and returns 
    the MST's size. 
    
    Since the MST is the smallest possible graph (including touching edges twice) between
    the remaining verticies, this will always return a distance less than or equal to the 
    actual distance to goal. 
    ''' 
    vertices = state.unexplored_vertices

    E = {}
    C = {}

    for v in vertices:  
        edges = state.get_edges(v)
        if edges == []:
            # no edge connecting v to earlier vertices, -1 is flag value
            E[v] = -1
            C[v] = sys.maxsize
        else:
            # the edge providing that cheapest connection
            E[v] = min(state.get_edges(v), key=lambda x: x[2])
            # the cheapest cost of a connection to v
            C[v] = E[v][2]
    
    F = set()
    size = 0
    Q = set(vertices)

    # while Q is not empty
    while Q:
        # Find and remove a vertex v from Q having the minimum possible 
        # value of C[v]
        v = min(Q, key=lambda x: C[x])
        Q.remove(v)

        # if not dead end
        if E[v] != -1:
            F.add(E[v])
            size += E[v][2]

            # Loop over the edges vw connecting v to other vertices w. For each 
            # such edge, if w still belongs to Q and vw has smaller weight than 
            # C[w], perform the following steps: ...

            for e in state.get_edges(v):
                # get other vertex in edge
                if e[0] == v:
                    w = e[1]
                else:
                    w = e[0]

                # ... set C[w] to the cost of edge vw, and
                # set E[w] to point to edge vw.
                if w in Q and e[2] < C[w]:
                    C[w] = e[2]
                    E[w] = e
    
    return size

def mixed(state):
    '''
    Heuristic 5: Two Shortest + MST

    Sum of the aforementioned - it is a closer approximation of true cost since 
    two shortest is an underestimate of the first and last edge in path, and
    MST is an underestimate of everything in the middle. Thus it is also an 
    underestimate of the total cost and admissible.
    '''
    return two_shortest(state) + mst(state)
  