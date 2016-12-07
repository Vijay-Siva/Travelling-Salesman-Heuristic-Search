from random import random
import sys

def rand(state):
    '''
    Note that min weight of an edge is 1
    '''
    return random(state.unexplored_vertices)


def get_min_edge_weight(edges):
    '''
    helper for next 2 functions
    '''
    if edges == []:
        return sys.maxsize

    # get min edge weight
    min_edge = edges[0]
    for e in edges:
        if min_edge[2] > e[2]:
            min_edge = e
    return min_edge[2]


def two_shortest(state):
    '''
    stortest edge connected to first, last on path
    '''
    return get_min_edge_weight(state.get_all_edges(state.path_vertices[0]))
    + get_min_edge_weight(state.get_all_edges(state.path_vertices[1]))

def greedy(state):
    '''
    Greedy heuristic takes a TSP instance and vertex, and calculates
    how far it is from it's nearest neighbour
    '''
    return get_min_edge_weight(state.get_edges(state.get_current_vertex()))

def mst(state):
    '''
    Size of mst of remaining vertices
    ''' 
    verticies = tsp.unexplored_vertices

    for v in vertices:  
        edges = get_edges(v)
        if edges == []:
            # no edge connecting v to earlier vertices, -1 is flag value
            E[v] = -1
            C[V] = sys.maxsize
        else:
            # the edge providing that cheapest connection
            E[v] = min(get_edges(v), key=lambda x: x.weight)
            # the cheapest cost of a connection to v
            C[V] = E[V].weight
    
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
            size += E[v].weight

            # Loop over the edges vw connecting v to other vertices w. For each 
            # such edge, if w still belongs to Q and vw has smaller weight than 
            # C[w], perform the following steps: ...

            for e in v.get_edges():
                # get other vertex in edge
                if e[0] == v:
                    w = e[1]
                else:
                    w = e[0]

                # ... set C[w] to the cost of edge vw, and
                # set E[w] to point to edge vw.
                if w in Q and e.weight < C[w]:
                    C[w] = e.weight
                    E[w] = e
    
    return size


 
  