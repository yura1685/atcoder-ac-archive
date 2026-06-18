N, M, K = map(int,input().split())
g = [set([i]) for i in range(N)]
for _ in range(M):
    u, v = map(int, input().split())
    g[u-1].add(v-1)
    g[v-1].add(u-1)

mod = 998244353
X = [0] * N
X[0] = 1

for _ in range(K):
    S = sum(X) % mod
    Y = [S] * N
    for u in range(N):
        for v in g[u]:
            Y[u] -= X[v]
        Y[u] %= mod
    X = Y.copy()

print(X[0])