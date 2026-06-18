from atcoder.dsu import DSU

N, X, Y = map(int,input().split())
P = [(0,0,X-1,Y-1)]
for _ in range(N):
    nex_P = []
    Q = input().split()
    A, B = int(Q[1]), int(Q[2])
    if Q[0] == 'X':
        for lx, ly, rx, ry in P:
            if rx < A:
                nex_P.append((lx, ly-B, rx, ry-B))
            elif A <= lx:
                nex_P.append((lx, ly+B, rx, ry+B))
            else:
                nex_P.append((lx, ly-B, A-1, ry-B))
                nex_P.append((A, ly+B, rx, ry+B))
    else:
        for lx, ly, rx, ry in P:
            if ry < A:
                nex_P.append((lx-B, ly, rx-B, ry))
            elif A <= ly:
                nex_P.append((lx+B, ly, rx+B, ry))
            else:
                nex_P.append((lx-B, ly, rx-B, A-1))
                nex_P.append((lx+B, A, rx+B, ry))
    P = nex_P.copy()

Size = len(P)
uf = DSU(Size)

for i in range(Size-1):
    for j in range(i+1, Size):
        lxi, lyi, rxi, ryi = P[i]
        lxj, lyj, rxj, ryj = P[j]
        if (rxi+1 == lxj or rxj+1 == lxi) and max(lyi,lyj) <= min(ryi,ryj):
            uf.merge(i,j)
        elif (ryi+1 == lyj or ryj+1 == lyi) and max(lxi,lxj) <= min(rxi,rxj):
            uf.merge(i,j)

ans = []
for g in uf.groups():
    s = 0
    for u in g:
        lx, ly, rx, ry = P[u]
        s += (rx-lx+1) * (ry-ly+1)
    ans.append(s)

ans.sort()
print(len(ans))
print(*ans)