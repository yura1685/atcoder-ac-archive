N = int(input())
inf = 10 ** 8
g = [[inf] * N for _ in range(N)]
for i in range(N): g[i][i] = 0
for _ in range(N-1):
    u, v = map(int, input().split())
    u, v = u-1, v-1
    g[u][v] = 1
    g[v][u] = 1
for j in range(N):
    for i in range(N):
        for k in range(N):
            g[i][k] = min(g[i][k], g[i][j] + g[j][k])

s = set()
for i in range(N):
    for j in range(i+1, N):
        if g[i][j] > 1 and g[i][j] % 2 == 1:
            s.add((i, j))

if len(s) % 2 == 1:
    print('First')
else:
    print('Second')
    u, v = map(int, input().split())
    if u == -1: exit()
    m, M = min(u, v) - 1, max(u, v) - 1
    s.discard((m, M))

while s:
    for m, M in s:
        print(m+1, M+1)
        s.discard((m, M))
        break
    u, v = map(int, input().split())
    if u == -1: exit()
    m, M = min(u, v) - 1, max(u, v) - 1
    s.discard((m, M))