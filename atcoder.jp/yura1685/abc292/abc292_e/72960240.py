from collections import deque

N, M = map(int,input().split())
g = [[] for _ in range(N+1)]
for _ in range(M):
    u, v = map(int,input().split())
    g[u].append(v)

cnt = [0] * (N+1)
for i in range(1,N+1):
    s = set([i])
    d = deque([i])
    while d:
        u = d.popleft()
        cnt[i] += 1
        for v in g[u]:
            if v in s:
                continue
            s.add(v)
            d.append(v)
        
ans = sum(cnt[i] - len(g[i]) - 1 for i in range(1,N+1))
print(ans)