from atcoder.dsu import DSU

N = int(input())
sx, sy, tx, ty = map(int,input().split())
circle = [list(map(int,input().split())) for _ in range(N)]
dsu = DSU(N)

for i in range(N-1):
    for j in range(i+1,N):
        x1,y1,r1 = circle[i]
        x2,y2,r2 = circle[j]
        d2 = (x1-x2)**2 + (y1-y2)**2
        if d2 > (r1+r2)**2 or d2 < (r1-r2)**2:
            continue
        dsu.merge(i,j)

sta = []
end = []

for i in range(N):
    x, y, r = circle[i]
    if (sx-x)**2 + (sy-y)**2 == r**2:
        sta.append(i)
    if (tx-x)**2 + (ty-y)**2 == r**2:
        end.append(i)

for s in sta:
    for t in end:
        if dsu.same(s,t):
            exit(print('Yes'))

print('No')