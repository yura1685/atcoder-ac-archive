from collections import deque

N, M = map(int,input().split())

g = [[] for _ in range(N)]
for _ in range(M):
    A, B = map(int,input().split())
    g[A-1].append(B-1)

ans = 0
for s in range(N):
    c = [0]*N
    c[s] = 1
    d = deque([s])
    while d:
        u = d.popleft()
        ans += 1
        for v in g[u]:
            if c[v] == 0:
                c[v] = 1
                d.append(v)

print(ans)