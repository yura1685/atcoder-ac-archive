from collections import deque

N, M = map(int,input().split())

g = [[] for _ in range(N)]
for _ in range(M):
    A, B = map(int,input().split())
    g[A-1].append(B-1)
    g[B-1].append(A-1)

X = [-1]*N

for i in range(N):
    if X[i] != -1:
        continue
    X[i] = 0
    d = deque([i])
    while d:
        u = d.popleft()
        for v in g[u]:
            if X[v] == -1:
                X[v] = 1-X[u]
                d.append(v)
            elif X[v] == X[u]:
                exit(print('No'))

print('Yes')