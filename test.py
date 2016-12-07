from tsp import *
from heuristics import * 
from search import * 

#TSP test cases 

Tests = [TSPState("Start", 0, None, [], [1, 2, 3, 4], [], 
            [(1, 2, 1), (2, 3, 1), (3, 4, 1), (4, 1, 1), (2, 4, 5), (1, 3, 7)], 4),
            TSPState("Start", 0, None, [], [1, 2, 3, 4], [], 
            [(1, 2, 10), (1, 3, 15), (1, 4, 20), (2, 1, 10), (2, 3, 35), (2, 4, 25),
                (3, 1, 15), (3, 2, 35), (3, 4, 30), (4, 1, 20), (4, 2, 25), 
                    (4, 3, 30)], 70)]


if __name__ == "__main__":
    se = SearchEngine('best_first', 'none')
    for test_case in Tests:
        final = se.search(initState=test_case, heur_fn=greedy, goal_fn=goal_state)