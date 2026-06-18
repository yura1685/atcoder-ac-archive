from itertools import permutations

N = int(input())

c = [i for i in range(1,N+1)]
p = list(permutations(c))
p.sort()
P = tuple(map(int,input().split()))
Q = tuple(map(int,input().split()))

print(abs(p.index(P)-p.index(Q)))