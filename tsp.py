python.linting.enabled = False

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

    