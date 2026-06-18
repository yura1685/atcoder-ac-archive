N = int(input())
g = [[0] * 1501 for _ in range(1501)]
for _ in range(N):
    x, y = map(int,input().split())
    g[x][y] += 1

for i in range(1501):
    for j in range(1501):
        if i > 0: g[i][j] += g[i-1][j]
        if j > 0: g[i][j] += g[i][j-1]
        if i > 0 and j > 0: g[i][j] -= g[i-1][j-1]

Q = int(input())
for _ in range(Q):
    a, b, c, d = map(int,input().split())
    print(g[c][d] - g[c][b-1] - g[a-1][d] + g[a-1][b-1])