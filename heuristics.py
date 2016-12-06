"""
Greedy (Heuristic) 
Complexity:O(n2log2(n))
Description: The Greedy heuristic gradually constructs a tour by repeatedly selecting the shortest edge and adding it to the tour as long as it doesn’t create a cycle with less than N edges, or increases the degree of any node to more than 2.
We must not add the same edge twice of course.

Pseudo code:
1. Sort all edges.
2. Select the shortest edge and add it to our tour if it doesn’t violate any of the above constraints.
3. Do we have N edges in our tour? If no, repeat step 2.

The Greedy algorithm normally keeps within 15-20% of the Held-Karp lower bound.
"""
def greedy():
    pass


"""
Insertion (Heuristic)  
Description: Insertion heuristics are quite straight forward, and there are many variants to choose from. The basics of insertion heuristics is to start with a tour of a subset of all cities, and then inserting the rest by some heuristic. The initial subtour is often a triangle or the convex hull. One can also start with a single edge as subtour.

(A) Nearest Insertion, O(n^2)
1. Select the shortest edge, and make a subtour of it.
2. Select a city not in the subtour, having the shortest distance to any one of the cities in the subtoor.
3. Find an edge in the subtour such that the cost of inserting the selected city between the edge’s cities will be minimal.
4. Repeat step 2 until no more cities remain.
"""
def nearest_insertion():
    pass


"""
(B) Convex Hull: O(n^2*log^2(n))
1. Find the convex hull of our set of cities, and make it our initial subtour.
2. For each city not in the subtour, find its cheapest insertion (as in step 3 of Nearest Insertion). Then chose the city with the least cost/increase ratio, and insert it.
3. Repeat step 2 until no more cities remain.
"""
def convex_hull():
    pass



"""
Nearest Neighbor (Heuristic)
Complexity: O(n^2)
Description: A weighted graph heuristic, always choose to visit the nearest neighbor.

Pseudo code:
1. Select a random city.
2. Find the nearest unvisited city and go there.
3. Are there any unvisitied cities left? If yes, repeat step 2.
4. Return to the first city.

The Nearest Neighbor algorithm will often keep its tours within 25% of the Held-Karp lower bound.
"""
def nearest_neighbours():
    pass
    