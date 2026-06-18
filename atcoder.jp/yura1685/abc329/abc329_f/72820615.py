N, Q = map(int,input().split())
C = [set()] + [set([int(x)]) for x in input().split()]
ind = [i for i in range(N+1)]

for _ in range(Q):
    x, y = map(int,input().split())
    a, b = ind[x], ind[y]
    if len(C[a]) <= len(C[b]):
        C[b] |= C[a]
        C[a].clear()
        print(len(C[b]))
    else:
        C[a] |= C[b]
        C[b].clear()
        ind[x], ind[y] = ind[y], ind[x]
        print(len(C[a]))
