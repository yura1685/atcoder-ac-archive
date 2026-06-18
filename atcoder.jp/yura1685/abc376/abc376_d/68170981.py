from collections import deque

N, M = map(int,input().split())
g = [[] for _ in range(N+1)]
for _ in range(M):
    a, b = map(int,input().split())
    g[a].append(b)
    
inf = float('inf')
ans = inf

for p in g[1]:
    s = set([p])
    d = deque()
    flag = False
    cnt = 1
    for u in g[p]:
        if u != 1:
            s.add(u)
            d.append((u,cnt+1))
    while d:
        u, x = d.popleft()
        if u == 1:
            ans = min(ans,x)
            break
        for v in g[u]:
            if v in s:
                continue
            s.add(v)
            d.append((v,x+1))

print(ans if ans < inf else -1)