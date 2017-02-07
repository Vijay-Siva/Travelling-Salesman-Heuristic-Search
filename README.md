# Travelling-Salesman-Heuristics

The Travelling salesman problem is a graph problem, where the goal is to find the shortest path that goes to each vertex exactly once and returns to the starting vertex in a weighted undirected graph. 

This project approached the TSP problem as a heuristic search, exploring different heuristics using an A\* search. 

## Table of Contents
  * [Heuristics](#heuristics)
    + [Random](#random)
    + [Greedy](#greedy)
    + [Two Shortest](#two-shortest)
    + [Minimum Spanning Tree (MST)](#minimum-spanning-tree--mst-)
    + [Mixed Two Shortest and Minimum Spanning Tree](#mixed-two-shortest-and-minimum-spanning-tree)

## Heuristics 

For our heuristic search, we created five different admissable heuristics. There is a description each of those heuristics below.  

### Random 

The random heuristic is a trivial algorithm, which randomly chooses the weight of one of the current vertices adjacent edges. This heuristic runs in constant time. 

### Greedy 

The greedy heuristic returns the weight of the minimum weight edge connecting the last vertex in the path to any of the unexplored vertices. This runs in O(E) time. 

### Two Shortest

The two shortest heuristic calculates the minimum edge connecting the last vertex in the path to the unexplored vertices, and the minimum edge connecting the first vertex in the path to any of the unexplored vertices. In the case that we are at the final step where we simply connect the last vertex in the path to the first vertex, our heuristic would double count because it will add the weight of the same edge twice. To avoid this, we instead simply return the minimum weight og one edge in this case. 

### Minimum Spanning Tree (MST)

The MST heuristic computes a minimum spanning tree between the remaining unexplored vertices in the graph, and returns the weight of this MST. 

### Mixed Two Shortest and Minimum Spanning Tree

This heuristic combines the MST heuristic and the two_shortest heuristic by simply adding their sums. 
