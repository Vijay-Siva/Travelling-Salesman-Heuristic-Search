#python.linting.enabled = False

from search import * 

class TSP(StateSpace):
    def __init__(self, action, gval, parent, vertices, edges, path):
        StateSpace.__init__(self, action, gval, parent)
        self.order = len(vertices) 
        self.vertices = vertices 
        self.edges = edges
        self.path = path
        return
    
    def successors(self):
        successors = [] 
        visited = Set()
        for edges in self.path:
            visited.add(edge[0])
        
        visited.add(self.path[-1][1])

        unvisited = [x for x in self.vertices and x not in visited]

        for vertex in visited:
            for edge in self.get_edges(vertex):
                if (edge[1] in unvisited):
                    new_state = TSP(str(edge), self.gval + edge[2], self, self.vertices, self.edges, path + [edge])
                    successors.append(new_state)

        return successors 

    def hashable_state(self):
        return hash((self.vertices, self.edges, self.path))
    
    '''Return all the outgoing edges for the given vertex in self.'''
    def get_edges(self, vertex):
        result = []
        for edge in self.edges:
            if (edge[0] == vertex):
                result.append(edge)
        return result

    ''' Get the current vertex in the path'''
    def get_current_vertex(self):
        if len(path) > 0:
            return path[-1][1]
        else:
            return None

    