from itertools import product, combinations

N, M = map(int,input().split())
rel = [tuple(map(int,input().split())) for _ in range(M)]
C = list(product([0,1],repeat=N))

ans = 0
for c in C:
    pick = []
    for i in range(N):
        if c[i] == 1:
            pick.append(i+1)
    np = len(pick)
    x = list(combinations(pick,2))
    if all([y in rel for y in x]):
        ans = max(ans,np)

print(ans)