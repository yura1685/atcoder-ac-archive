from collections import Counter
from bisect import *

H, W, M = map(int,input().split())

x, y, xy = [], [], []
for _ in range(M):
    h, w = map(int,input().split())
    x.append(h)
    y.append(w)
    xy.append((h,w))
    
xy.sort()

cx = dict(Counter(x))
cy = dict(Counter(y))

xm = max(cx.values())
ym = max(cy.values())

X = [xx for xx in cx if cx[xx] == xm]
Y = [yy for yy in cy if cy[yy] == ym]

ans = xm + ym - 1
for x in X:
    for y in Y:
        if bisect(xy,(x,y)) == bisect_left(xy,(x,y)):
            print(ans+1)
            exit()
            
print(ans)