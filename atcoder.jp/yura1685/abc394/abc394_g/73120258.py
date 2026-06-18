from atcoder.dsu import DSU

H, W = map(int,input().split())
F = [list(map(int,input().split())) for _ in range(H)]
M = max(max(L) for L in F)

def d(h,w): return h*W + w

E = [[] for _ in range(M+1)]
for h in range(H):
    for w in range(W):
        if h + 1 < H:
            h_min = min(F[h][w], F[h+1][w])
            E[h_min].append((d(h,w), d(h+1,w)))
        if w + 1 < W:
            w_min = min(F[h][w], F[h][w+1])
            E[w_min].append((d(h,w), d(h,w+1)))

query = []
Q = int(input())
for _ in range(Q):
    A, B, Y, C, D, Z = map(int,input().split())
    query.append([d(A-1, B-1), d(C-1, D-1), Y, Z, 1, M+1])

for _ in range(20):
    midlist = [[] for _ in range(M+1)]
    flag = True
    for i in range(Q):
        q = query[i]
        if q[5] - q[4] > 1:
            mid = (q[4] + q[5]) // 2
            midlist[mid].append(i)
            flag = False
    if flag:
        break
    uf = DSU(H*W)
    for h in range(M, 0, -1):
        for u, v in E[h]:
            uf.merge(u, v)
        for ind in midlist[h]:
            if uf.same(query[ind][0],query[ind][1]):
                query[ind][4] = h
            else:
                query[ind][5] = h

for q in query:
    u, v, Y, Z, ok, ng = q
    m = min(Y, Z, ok)
    print(Y + Z - 2*m)