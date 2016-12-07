from tsp import *
from heuristics import * 
from search import * 

#TSP test cases 

Problems = TSPState("Start", 0, None, [], [1, 2, 3, 4], [], 
            [(1, 2, 1), (2, 3, 1), (3, 2, 1), (4, 1, 1), (2, 4, 5), (1, 3, 7)], 4)



if __name__ == "__main__":
    se = SearchEngine('best_first', 'full')
    final = se.search(initState=Problems, heur_fn=greedy, goal_fn=goal_state)
    print(final)

