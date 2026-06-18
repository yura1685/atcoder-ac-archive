from atcoder.dsu import DSU

N, Q = map(int,input().split())
dsu = DSU(N) # 0-indexed
BC = [0]*N  # その頂点が黒か否か
BL = [0]*N  # その頂点がリーダーであるとき、グループの黒の個数

for _ in range(Q):
    a, *q = map(int,input().split())
    if a == 1:
        u, v = q[0]-1, q[1]-1
        x, y = dsu.leader(u), dsu.leader(v)
        if x == y:
            continue
        dsu.merge(u,v)
        z = dsu.leader(u)
        if x == z:
            BL[x] += BL[y]
            BL[y] = 0
        else:
            BL[y] += BL[x]
            BL[x] = 0
    elif a == 2:
        u = q[0] - 1
        if BC[u] == 0:
            BC[u] += 1
            BL[dsu.leader(u)] += 1
        else:
            BC[u] -= 1
            BL[dsu.leader(u)] -= 1
    else:
        u = q[0] - 1
        print('Yes' if BL[dsu.leader(u)] else 'No')