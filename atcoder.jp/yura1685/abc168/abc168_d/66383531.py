from collections import deque

N, M = map(int,input().split())

g = [[] for _ in range(N)]
route = [-1]*N
serch = deque([1])
route[0] = 1

for _ in range(M):
    A, B = map(int,input().split())
    g[A-1].append(B)
    g[B-1].append(A)

while serch:
    u = serch.popleft()
    for v in g[u-1]:
        if route[v-1] == -1:
            route[v-1] = u
            serch.append(v)

if min(route) == -1:
    print('No')
else:
    print('Yes')
    for i in range(1,N):
        print(route[i])