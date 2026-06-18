N = int(input())
g = [[] for _ in range(N)]
dim = [0] * N
s = set()
for _ in range(N-1):
    u, v = map(int,input().split())
    u, v = u-1, v-1
    g[u].append(v)
    g[v].append(u)
    if dim[u] == 1: s.discard(u)
    if dim[v] == 1: s.discard(v)
    dim[u] += 1
    dim[v] += 1
    if dim[u] == 1: s.add(u)
    if dim[v] == 1: s.add(v)

ans = []
while s:
    x = s.pop()
    for u in g[x]:
        if dim[u] > 0:
            break
    ans.append(dim[u])
    for v in g[u]:
        if dim[v] == 1:
            dim[v] = 0
            s.discard(v)
        else:
            for w in g[v]:
                if w != u:
                    break
            dim[w] -= 1
            s.add(w)
            dim[v] = 0

ans.sort()
print(*ans)