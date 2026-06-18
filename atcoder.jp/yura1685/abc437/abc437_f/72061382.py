from atcoder.segtree import SegTree

N, Q = map(int,input().split())
X, Y = [], []
for _ in range(N):
    x, y = map(int,input().split())
    X.append(x+y)
    Y.append(x-y)

inf = float('inf') 
plusM = SegTree(max, -inf, X)
plusm = SegTree(min,  inf, X)
minuM = SegTree(max, -inf, Y)
minum = SegTree(min,  inf, Y)

for _ in range(Q):
    q = list(map(int,input().split()))
    if q[0] == 1:
        i, x, y = q[1:]
        plusM.set(i-1, x+y)
        plusm.set(i-1, x+y)
        minuM.set(i-1, x-y)
        minum.set(i-1, x-y)
        continue
    L, R, x, y = q[1:]
    L -= 1
    P = x + y
    M = x - y
    print(max(abs(plusM.prod(L,R) - P),
              abs(plusm.prod(L,R) - P),
              abs(minuM.prod(L,R) - M),
              abs(minum.prod(L,R) - M)))