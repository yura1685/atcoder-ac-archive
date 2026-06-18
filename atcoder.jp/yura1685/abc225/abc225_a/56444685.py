import itertools
S = list(input())
U = list(itertools.permutations(S,3))
print(len(set(U)))