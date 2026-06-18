from collections import deque

N = int(input())
g = [[] for _ in range(N)]

for _ in range(N-1):
    u, v, w = map(int,input().split())
    g[u-1].append((v-1,w % 2))
    g[v-1].append((u-1,w % 2))

c = [-1] * N; c[0] = 0
check = [0] * N; check[0] = 1

d = deque([(0, 0)])    # (頂点, 色)

while d:
    u, color = d.popleft()
    for v, w in g[u]:
        if check[v]:
            continue
        c[v] = c[u] ^ w
        d.append((v, c[v]))
        check[v] = 1

for i in c:
    print(i)