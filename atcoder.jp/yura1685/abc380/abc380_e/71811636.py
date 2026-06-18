from atcoder.dsu import DSU

N, Q = map(int,input().split())
uf = DSU(N+2)
co = [i for i in range(N+2)]
ra = [(i,i) for i in range(N+2)]
cn = [1] * (N+2)
for _ in range(Q):
    q = list(map(int,input().split()))
    if q[0] == 1:
        u, c = q[1:]
        v = uf.leader(u)
        l, r = ra[v]
        cl = co[v]

        cn[c]  += r - l + 1
        cn[cl] -= r - l + 1     
        co[v] = c
        l2, r2 = l, r
        ll = uf.leader(l-1)
        if co[ll] == c:
            nl, nr = ra[ll]
            l2 = min(l2, nl)
            v = uf.merge(v,ll)

        rl = uf.leader(r+1)
        if co[rl] == c:
            nl, nr = ra[rl]
            r2 = max(r2, nr)
            v = uf.merge(v,rl)
        
        v = uf.leader(v)
        ra[v] = (l2,r2)
        co[v] = c

    else:
        c = q[1]
        print(cn[c])
