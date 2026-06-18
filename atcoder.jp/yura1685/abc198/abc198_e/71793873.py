from collections import defaultdict

N = int(input())
C = list(map(int,input().split()))
g = [[] for _ in range(N)]
for _ in range(N-1):
    A, B = map(int,input().split())
    g[A-1].append(B-1)
    g[B-1].append(A-1)

ans = []

check = [0]*N
d = defaultdict(int)
dfs = [(0,0)]
while dfs:
    u, s = dfs.pop()
    if s == 0:
        check[u] = 1
        if d[C[u]] == 0:
            ans.append(u)
        d[C[u]] += 1
        dfs.append((u,1))
        for v in g[u]:
            if not check[v]:
                dfs.append((v,0))
    else:
        d[C[u]] -= 1

ans.sort()
for a in ans:
    print(a+1)