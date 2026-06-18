from collections import defaultdict

N, C = map(int,input().split())
D = [list(map(int,input().split())) for _ in range(C)]
c = [list(map(int,input().split())) for _ in range(N)]

d0, d1, d2 = defaultdict(int), defaultdict(int), defaultdict(int)
for h in range(N):
    for w in range(N):
        if (h+w) % 3 == 0:
            d0[c[h][w]-1] += 1
        elif (h+w) % 3 == 1:
            d1[c[h][w]-1] += 1
        else:
            d2[c[h][w]-1] += 1

def f(i, t):
    res = 0
    if i == 0:
        for col, cnt in d0.items():
            res += D[col][t] * cnt
    if i == 1:
        for col, cnt in d1.items():
            res += D[col][t] * cnt
    if i == 2:
        for col, cnt in d2.items():
            res += D[col][t] * cnt
    return res

F = [[-1] * C for _ in range(3)]
for i in range(3):
    for t in range(C):
        F[i][t] = f(i, t)

ans = float('inf')
for p in range(C):
    for q in range(C):
        for r in range(C):
           if (p == q or q == r or r == p):
               continue
           ans = min(ans, F[0][p] + F[1][q] + F[2][r])

print(ans)