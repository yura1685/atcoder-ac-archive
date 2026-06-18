from atcoder.dsu import DSU

N, M = map(int,input().split())
E = [[0]*N for _ in range(N)]
for _ in range(M):
    x, y = map(int,input().split())
    E[x-1][y-1] = 1
    E[y-1][x-1] = 1

ans = 0
for i in range(1<<(N-1)):
    A, B = [N-1], []
    for bit in range(N-1):
        if (i >> bit) & 1:
            A.append(bit)
        else:
            B.append(bit)
    uf = DSU(N)
    for a in A:
        for b in B:
            if E[a][b]:
                uf.merge(a,b)
    if len(uf.groups()) == 1:
        ans += 1

print(ans)