from atcoder.lazysegtree import LazySegTree
def pl(x, y): return x + y

N = int(input())
g = [[] for _ in range(N)]
Edge = []
for _ in range(N-1):
    u, v, w = map(int, input().split())
    u, v = u-1, v-1
    g[u].append((v, w))
    g[v].append((u, w))
    Edge.append((u, v))

K = N.bit_length()
parent = [[-1] * N for _ in range(K)]
node_depth = [0] * N

go = [-1] * N
ba = [-1] * N
_depth = [0] * N
step = 0
stack = [(0, -1, 0, 0, True)]
while stack:
    u, f, w, d, b = stack.pop()
    if b == True:
        stack.append((u, f, w, d, False))
        go[u] = step
        _depth[u] = (_depth[f] if f != -1 else 0) + w
        node_depth[u] = d
        parent[0][u] = f
        for v, w2 in g[u]:
            if v == f:
                continue
            stack.append((v, u, w2, d+1, True))
    else:
        ba[u] = step
    step += 1

for k in range(K-1):
    for i in range(N):
        if parent[k][i] != -1:
            parent[k+1][i] = parent[k][parent[k][i]]

def lca(u, v):
    if node_depth[u] < node_depth[v]:
        u, v = v, u
    for k in range(K):
        if (node_depth[u] - node_depth[v]) >> k & 1:
            u = parent[k][u]
    if u == v: return u
    for k in range(K-1, -1, -1):
        if parent[k][u] != parent[k][v]:
            u = parent[k][u]
            v = parent[k][v]
    return parent[0][u]

depth = [0] * (2 * N)
for u in range(N):
    depth[go[u]] = depth[ba[u]] = _depth[u]

lst = LazySegTree(pl, 0, pl, pl, 0, depth)

Q = int(input())
for _ in range(Q):
    q, x, y = map(int, input().split())
    if q == 1:
        i, new_w = x-1, y
        u, v = Edge[i]
        child = v if node_depth[v] > node_depth[u] else u
        p = parent[0][child]
        now_w = lst.get(go[child]) - lst.get(go[p])
        diff_w = new_w - now_w
        lst.apply(go[child], ba[child] + 1, diff_w)
    else:
        u, v = x-1, y-1
        Lca = lca(u, v)
        dist = lst.get(go[u]) + lst.get(go[v]) - 2 * lst.get(go[Lca])
        print(dist)
