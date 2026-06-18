N, M, L = map(int,input().split())
inf = 10 ** 10
g = [[inf] * N for _ in range(N)]
for i in range(N):
    g[i][i] = 0
for _ in range(M):
    a, b, c = map(int,input().split())
    g[a-1][b-1] = c
    g[b-1][a-1] = c

for k in range(N):
    for i in range(N):
        for j in range(N):
            if g[i][j] > g[i][k] + g[k][j]:
                g[i][j] = g[i][k] + g[k][j]

d = [[inf]*N for _ in range(N)]

for i in range(N):
    d[i][i] = 0
    for j in range(N):
        if i == j:
            continue
        if g[i][j] <= L:
            d[i][j] = 1
    

for k in range(N):
    for i in range(N):
        for j in range(N):
            if d[i][j] > d[i][k] + d[k][j]:
                d[i][j] = d[i][k] + d[k][j]

Q = int(input())
for _ in range(Q):
    s, t = map(int,input().split())
    print(d[s-1][t-1] - 1 if d[s-1][t-1] < inf else -1)