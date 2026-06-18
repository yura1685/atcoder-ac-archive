from sortedcontainers import SortedList

H, W, N = map(int,input().split())
XY = [SortedList() for _ in range(H+1)]
YX = [SortedList() for _ in range(W+1)]

for _ in range(N):
    X, Y = map(int,input().split())
    XY[X].add(Y)
    YX[Y].add(X)

Q = int(input())
for _ in range(Q):
    a, b = map(int,input().split())
    if a == 1:
        for y in XY[b]:
            YX[y].discard(b)
        print(len(XY[b]))
        XY[b].clear()
    if a == 2:
        for x in YX[b]:
            XY[x].discard(b)
        print(len(YX[b]))
        YX[b].clear()        