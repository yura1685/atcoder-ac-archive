from collections import deque
N, M = map(int,input().split())

G = [[] for _ in range(N+1)]
c = [0]*(N+1)

for _ in range(M):
    X, Y = map(int,input().split())
    G[Y].append(X)

Q = int(input())
for _ in range(Q):
    q, x = map(int,input().split())
    if q == 1:
        if c[x] == 1:
            continue
        c[x] = 1
        d = deque([x])
        while d:
            u = d.popleft()
            for v in G[u]:
                if c[v] == 0:
                    c[v] = 1
                    d.append(v)
    else:
        print('Yes' if c[x] else 'No')