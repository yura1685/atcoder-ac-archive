N, M, K, S, T, X = map(int,input().split())
S, T, X = S-1, T-1, X-1
g = [[] for _ in range(N)]
for _ in range(M):
    U, V = map(int,input().split())
    g[U-1].append(V-1)
    g[V-1].append(U-1)

# dp[i][j][k]: Sから辺をi回通ってjに行くとき、Xをk (mod 2) 回通るもの

dp = [[[0,0] for _ in range(N+1)] for _ in range(K+1)]

dp[0][S][0] = 1
mod = 998244353
for i in range(K):
    for j in range(N):
        if j != X:
            for u in g[j]:
                for x in range(2):
                    dp[i+1][j][x] += dp[i][u][x]
                    dp[i+1][j][x] %= mod
        else:
            for u in g[X]:
                for x in range(2):
                    dp[i+1][X][x] += dp[i][u][1-x]
                    dp[i+1][X][x] %= mod

print(dp[K][T][0])