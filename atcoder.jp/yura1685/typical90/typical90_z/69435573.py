from random import randint
from sys import setrecursionlimit
setrecursionlimit(10**8)

N = int(input())
g = [[] for _ in range(N)]
col = [-1] * N

for _ in range(N-1):
    a, b = map(int,input().split())
    g[a-1].append(b-1)
    g[b-1].append(a-1)

def dfs(u, c):
    for v in g[u]:
        if col[v] == -1:
            col[v] = 1 - c
            dfs(v, 1-c)

p = randint(1,N-1)
col[p] = 0
dfs(p,0)

pick = -1

if col.count(0) >= N//2:
    pick = 0
else:
    pick = 1

ans = []
cnt = 0
for i in range(N):
    if col[i] == pick:
        ans.append(i+1)
        cnt += 1
    if cnt == N//2:
        exit(print(*ans))