from itertools import permutations

N = int(input())
P = tuple(map(int,input().split()))
Q = tuple(map(int,input().split()))
C = list(permutations([i+1 for i in range(N)]))
print(abs(C.index(P)-C.index(Q)))