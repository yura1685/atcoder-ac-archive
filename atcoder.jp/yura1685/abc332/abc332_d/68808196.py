from itertools import permutations

H, W = map(int,input().split())
A = [list(map(int,input().split())) for _ in range(H)]
B = [list(map(int,input().split())) for _ in range(H)]

def f(X):
    X = list(X)
    n = len(X)
    L = [i for i in range(n)]
    res = 0
    for i in range(n-1):
        if L[i] == X[i]:
            continue
        for j in range(n-1,i,-1):
            if X[j] == i:
                X[j-1], X[j] = X[j], X[j-1]
                res += 1
    return res

for p in permutations(i for i in range(H)):
    for q in permutations(j for j in range(W)):
        C = [[A[i][j] for j in q] for i in p]
        if B == C: exit(print(f(p)+f(q)))
print(-1)

