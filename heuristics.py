
def rand(tsp, vertex):
    pass

def two_shortest(tsp, vertex):
    #stortest edge connected to first, last on path
    pass

def greedy(tsp, vertex):
    '''
    Greedy heuristic takes a TSP instance and vertex, and calculates
    how far it is from it's nearest neighbour
    '''
    edges = tsp.get_edges(vertex)

    # dead end
    if edges == []:
        return sys.maxint
    min_edge = edges[0]
    for e in edges:
        if min_edge.weight > e.weight:
            min_edge = e
    return e


'''Associate with each vertex v of the graph a number C[v] 
(the cheapest cost of a connection to v) and an edge E[v] 
(the edge providing that cheapest connection). To initialize 
these values, set all values of C[v] to +∞ (or to any number 
larger than the maximum edge weight) and set each E[v] to a 
special flag value indicating that there is no edge connecting 
v to earlier vertices.

Initialize an empty forest F and a set Q of vertices that have 
not yet been included in F (initially, all vertices).
Repeat the following steps until Q is empty:
Find and remove a vertex v from Q having the minimum possible 
value of C[v]

Add v to F and, if E[v] is not the special flag value, also add E[v] 
to F

Loop over the edges vw connecting v to other vertices w. For each 
such edge, if w still belongs to Q and vw has smaller weight than 
C[w], perform the following steps:

Set C[w] to the cost of edge vw
Set E[w] to point to edge vw.
Return F
''''
for v in tsp.vertices:
    E[v] = min(get_edges(v), key: lambda x: x.weight)
    C[V] = E[V].weight
