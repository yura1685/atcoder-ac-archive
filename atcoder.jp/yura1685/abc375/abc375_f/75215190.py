N, M, Q = map(int, input().split())
e = set(range(M))
inf = 10 ** 18
g = [[inf] * N for _ in range(N)]
for i in range(N):
    g[i][i] = 0
Edge = []
for _ in range(M):
    a, b, c = map(int, input().split())
    Edge.append((a-1, b-1, c))
Query = []
for _ in range(Q):
    q = [int(x) - 1 for x in input().split()]
    if q[0] == 0:
        e.discard(q[1])
    Query.append(q)

for i in e:
    u, v, w = Edge[i]
    g[u][v] = g[v][u] = w 

for j in range(N):
    for i in range(N):
        for k in range(N):
            g[i][k] = min(g[i][k], g[i][j] + g[j][k])

ans = []
while Query:
    if Query[-1][0] == 1:
        q, x, y = Query.pop()
        ans.append(g[x][y] if g[x][y] < inf else -1)
    else:
        q, i = Query.pop()
        u, v, w = Edge[i]
        if w < g[u][v]:
            g[u][v] = g[v][u] = w
            for x in range(N):
                for y in range(N):
                    g[x][y] = min(g[x][y], 
                                  g[x][u] + w + g[v][y], 
                                  g[x][v] + w + g[u][y])

ans.reverse()
print(*ans, sep='\n')