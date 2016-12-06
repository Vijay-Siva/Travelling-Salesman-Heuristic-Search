from search import * 
class TSP():
   def __init__(self, vertices, edges, path=[]):
       self.order = len(vertices) 
       self.vertices = vertices 
       self.edges = edges
       self.path = path
    
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

    