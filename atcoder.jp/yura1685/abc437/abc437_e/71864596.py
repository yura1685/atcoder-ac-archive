from sys import setrecursionlimit
setrecursionlimit(10**8)

N = int(input())
g = [[] for _ in range(N+1)]

for i in range(1,N+1):
    x, y = map(int,input().split())
    g[x].append((y,i))

ans = []

def dfs(now):
    for u in now:
        if u: ans.append(u)
    nex = []
    for u in now:
        for y, v in g[u]:
            nex.append((y,v))
    if not nex: return
    nex.sort()
    s = 0
    M = len(nex)
    while s < M:
        e = s
        n = nex[s][0]
        hoge = []
        while e < M and nex[e][0] == n:
            hoge.append(nex[e][1])
            e += 1
        dfs(hoge)
        s = e

dfs([0])
print(*ans)