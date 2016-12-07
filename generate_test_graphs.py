from random import random, shuffle
from math import ceil

MAX_WEIGHT = 5

E = []
V = []

# generate a list of verices in random order
for i in range(49):
    V.append(i+1)
V.append(i+2)
shuffle(V)

# create trivial Hamiltonian cycle (connect all vertices
# with edges of weight 1)
for i in range(49):
    E.append((V[i], V[i+1], 1))
E.append((V[i+1], V[0], 1))

for i in range(49):
    E.append((V[i], V[i+1], ceil(MAX_WEIGHT*random())))
E.append((V[i+1], V[0], ceil(MAX_WEIGHT*random())))

print(E)
print(V)