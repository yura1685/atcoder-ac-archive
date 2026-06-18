from itertools import combinations

H1, W1 = map(int,input().split())
A = [list(map(int,input().split())) for _ in range(H1)]
H2, W2 = map(int,input().split())
B = [list(map(int,input().split())) for _ in range(H2)]

for P in combinations([i for i in range(H1)], H2):
    for Q in combinations([i for i in range(W1)], W2):
        C = [[A[p][q] for q in Q] for p in P]
        if B == C:
            exit(print('Yes'))
print('No')