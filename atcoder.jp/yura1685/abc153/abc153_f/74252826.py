from atcoder.lazysegtree import LazySegTree
from bisect import *

def pl(x, y): return x + y

N, D, A = list(map(int, input().split()))
D = 2 * D
XH = []
for _ in range(N):
    X, H = map(int, input().split())
    XH.append((X, H))
XH.sort()
X = [XH[i][0] for i in range(N)]
H = [XH[i][1] for i in range(N)]

lst = LazySegTree(pl, 0, pl, pl, 0, H)
L = 0
ans = 0
while L < N:
    h = lst.get(L)
    if h <= 0:
        pass
    else:
        l = X[L]
        R = bisect_right(X, l + D)
        num = (h + A - 1) // A
        lst.apply(L, R, - num * A)
        ans += num
    L += 1

print(ans)