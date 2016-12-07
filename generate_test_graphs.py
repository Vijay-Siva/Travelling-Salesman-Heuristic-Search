from random import random
from math import ceil

E = []
V = []


for i in range(49):
    E.append(i+1)
E.append(i+2)

# add Hamiltonian cycle
for i in range(49):
    E.append(i+1)
    V.append([i+1, i+2, ceil(5*random())])

# add Hamiltonian cycle
for i in range(49):
    E.append(i+1)
    V.append([i+1, i+2, ceil(5*random())])

# add Hamiltonian cycle
for i in range(49):
    E.append(i+1)
    V.append([i+1, i+2, ceil(5*random())])


# add noise
for i in range(50):
    V.append([ceil(50*random()), ceil(50*random()), ceil(5*random())])

print(E)
print(V)