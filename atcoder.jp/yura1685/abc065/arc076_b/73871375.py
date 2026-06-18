from atcoder.dsu import DSU

N = int(input())
P_xy, P_yx = [], []
for i in range(N):
    x, y = map(int, input().split())
    P_xy.append((x,y,i))
    P_yx.append((y,x,i))
P_xy.sort()
P_yx.sort()

E = []
for i in range(N-1):
    x1, y1, i1 = P_xy[i]
    x2, y2, i2 = P_xy[i+1]
    E.append((min(abs(x1-x2), abs(y1-y2)), i1, i2))
    x1, y1, i1 = P_yx[i]
    x2, y2, i2 = P_yx[i+1]
    E.append((min(abs(x1-x2), abs(y1-y2)), i1, i2))

E.sort()

ans = 0
uf = DSU(N)
for c, i, j in E:
    if not uf.same(i, j):
        uf.merge(i, j)
        ans += c

print(ans)