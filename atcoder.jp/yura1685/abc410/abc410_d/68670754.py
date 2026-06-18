from collections import deque

N, M = map(int,input().split())
g = [[] for _ in range(N+1)]
for _ in range(M):
    A, B, W = map(int,input().split())
    g[A-1].append((B-1,W))

s = set()
d = deque(); d.append((0,0))

while d:
    u, score = d.popleft()
    if (u, score) in s:
        continue
    s.add((u,score))
    for v, w in g[u]:
        d.append((v,score^w))

for i in range(1025):
    if (N-1,i) in s:
        exit(print(i))
print(-1)