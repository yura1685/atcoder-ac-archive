import sys
sys.setrecursionlimit(10**8)
mod = 10**9 + 7

N = int(input())
g = [[] for _ in range(N+1)]
for _ in range(N-1):
    a, b = map(int,input().split())
    g[a].append(b)
    g[b].append(a)

def dfs(u,f):
    B, W = 1, 1
    for v in g[u]:
        if v == f:
            continue
        b, w = dfs(v,u)
        W *= b + w
        B *= w
        W %= mod
        B %= mod
    return B, W

B, W = dfs(1,0)
print((B+W)%mod)