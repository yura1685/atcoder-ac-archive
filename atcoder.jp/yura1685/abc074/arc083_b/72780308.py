N = int(input())
A = [list(map(int,input().split())) for _ in range(N)]
R = []
for i in range(N-1):
    for j in range(i+1,N):
        R.append((A[i][j], i, j))
R.sort()

inf = float('inf')
X = [[inf]*N for _ in range(N)]
for i in range(N): X[i][i] = 0

build = 0
for w, u, v in R:
    if w < X[u][v]:
        X[u][v] = X[v][u] = w
        build += w
        for i in range(N-1):
            for j in range(i+1,N):
                m = min(X[i][j],
                        X[i][u] + X[u][v] + X[v][j],
                        X[i][v] + X[v][u] + X[u][j])
                X[i][j] = m
                X[j][i] = m

print(build if A == X else -1)