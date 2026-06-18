N, M = map(int, input().split())
g = [set() for _ in range(N)]
E = []
for _ in range(M):
    u, v = map(int, input().split())
    u, v = u-1, v-1
    g[u].add(v)
    g[v].add(u)
    E.append((u, v))
Q = int(input())
X = [int(x) - 1 for x in input().split()]
leader = list(range(N))

def find(x):
    root = x
    while leader[root] != root:
        root = leader[root]
    now = x
    while now != root:
        nex = leader[now]
        leader[now] = root
        now = nex
    return root

edge = M
for x in X:
    u, v = E[x]
    u, v = find(u), find(v)
    if u == v or v not in g[u]:
        pass
    else:
        degu = len(g[u])
        degv = len(g[v])
        if degu > degv:
            u, v = v, u
        leader[u] = v
        s = g[u]

        for w in s:
            g[w].discard(u)
            if w == v:
                edge -= 1
            elif w in g[v]:
                edge -= 1
            else:
                g[w].add(v)
                g[v].add(w)
        g[u].clear()
    print(edge)