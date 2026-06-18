N, Q = map(int,input().split())
g = [set() for _ in range(N+1)]
ans = N
for _ in range(Q):
    q = list(map(int,input().split()))
    if q[0] == 1:
        u, v = q[1:]
        if not g[u]: ans -= 1
        if not g[v]: ans -= 1
        g[u].add(v)
        g[v].add(u)
    else:
        u = q[1]
        if g[u]: ans += 1
        for v in g[u]:
            g[v] -= {u}
            if not g[v]: ans += 1
        g[u].clear()
    print(ans)