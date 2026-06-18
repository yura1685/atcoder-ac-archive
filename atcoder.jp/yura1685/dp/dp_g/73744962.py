from sys import setrecursionlimit
setrecursionlimit(10**6)

N, M = map(int,input().split())
g = [[] for _ in range(N)]
for _ in range(M):
    x, y = map(int,input().split())
    g[x-1].append(y-1)

dp = [-1] * N

def depth(u):
    if dp[u] != -1:
        return dp[u]
    
    if not g[u]:
        dp[u] = 0
        return 0
    
    res = 0
    for v in g[u]:
        res = max(res, depth(v))
    dp[u] = res + 1
    return res + 1

for i in range(N):
    if dp[i] == -1:
        depth(i)

print(max(dp))