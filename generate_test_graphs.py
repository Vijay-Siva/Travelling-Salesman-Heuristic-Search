from random import random, shuffle
from math import ceil

MAX_WEIGHT = 5

def create_test(num_vertices, branch_factor):
    E = []
    V = []

    # generate a list of verices in random order
    for i in range(num_vertices):
        V.append(i+1)
    shuffle(V)

    # create trivial Hamiltonian cycle (connect all vertices
    # with edges of weight 1)
    for i in range(num_vertices-1):
        E.append((V[i], V[i+1], 1))
    E.append((V[i+1], V[0], 1))

    for n in range(branch_factor-1):
        for i in range(num_vertices-1):
            E.append((V[i], V[i+1], ceil(MAX_WEIGHT*random())))
        E.append((V[i+1], V[0], ceil(MAX_WEIGHT*random())))

    print("TSPState(\"Start\", 0, None, [], " + str(V) + ", [], " + str(E) + ", " + str(num_vertices) + ")")


# we redirect output of this program to a txt file to get these tests
create_test(5, 1)
create_test(5, 2)
create_test(5, 3)
create_test(5, 5)
create_test(5, 10)

create_test(5, 1)
create_test(5, 2)
create_test(5, 3)
create_test(5, 5)
create_test(5, 10)

create_test(5, 1)
create_test(5, 2)
create_test(5, 3)
create_test(5, 5)
create_test(5, 10)

create_test(5, 1)
create_test(5, 2)
create_test(5, 3)
create_test(5, 5)
create_test(5, 10)

create_test(5, 1)
create_test(5, 2)
create_test(5, 3)
create_test(5, 5)
create_test(5, 10)



create_test(10, 1)
create_test(10, 2)
create_test(10, 3)
create_test(10, 4)

create_test(10, 1)
create_test(10, 2)
create_test(10, 3)
create_test(10, 4)

create_test(10, 1)
create_test(10, 2)
create_test(10, 3)
create_test(10, 4)

create_test(10, 1)
create_test(10, 2)
create_test(10, 3)
create_test(10, 4)

create_test(10, 1)
create_test(10, 2)
create_test(10, 3)
create_test(10, 4)




create_test(15, 1)
create_test(15, 2)

create_test(15, 1)
create_test(15, 2)

create_test(15, 1)
create_test(15, 2)

create_test(15, 1)
create_test(15, 2)

create_test(15, 1)
create_test(15, 2)

create_test(15, 1)
create_test(15, 2)


print("MST tests")

create_test(5, 10)
create_test(10, 10)
create_test(15, 10)

