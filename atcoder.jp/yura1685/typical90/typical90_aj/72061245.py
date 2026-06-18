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
    q = int(input()) - 1
    P = X[q]
    M = Y[q]
    print(max(abs(plusM.all_prod() - P),
              abs(plusm.all_prod() - P),
              abs(minuM.all_prod() - M),
              abs(minum.all_prod() - M)))