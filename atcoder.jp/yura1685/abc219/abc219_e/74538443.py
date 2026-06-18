from atcoder.dsu import DSU

A = []
for _ in range(4):
    for n in map(int, input().split()):
        A.append(n)
A.reverse()
House = 0
for i in range(16):
    if A[i] == 1:
        House |= (1 << i)

ans = 0
s = {0,1,2,3,
     4,    7,
     8,    11,
     12,13,14,15}

for Area in range(1, 1 << 16):
    if House & Area != House:
        continue

    uf = DSU(16)
    idx = -1
    for i in range(16):
        if (Area >> i) & 1:
            idx = i
        h, w = divmod(i, 4)
        if w < 3 and (Area >> (i+1)) & 1 == (Area >> i) & 1:
            uf.merge(i, i+1)
        if h < 3 and (Area >> (i+4)) & 1 == (Area >> i) & 1:
            uf.merge(i, i+4)
    
    if uf.size(idx) != Area.bit_count():
        continue

    L = uf.leader(idx)

    for G in uf.groups():
        if uf.leader(G[0]) == L:
            continue
        for u in G:
            if u in s:
                break
        else:
            break
    else:
        ans += 1

print(ans)