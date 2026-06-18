from itertools import permutations

N = int(input())
k = int(input())
Cs = [input() for _ in range(N)]
S = set()

for P in permutations(range(N)):
    Q = P[:k]
    s = ''
    for p in Q:
        s += Cs[p]
    S.add(s)
    
print(len(S))