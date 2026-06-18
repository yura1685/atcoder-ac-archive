from atcoder.segtree import SegTree
from bisect import bisect_left, bisect_right

N, W, L, R = map(int,input().split())
X = [0] + list(map(int,input().split())) + [W]
def op(x, y): return x+y
st = SegTree(op, 0, [0]*(N+2))
st.set(0, 1)

for i in range(1,N+2):
    x = X[i]
    l, r = bisect_left(X, x-R), bisect_right(X, x-L)
    if l == r: continue
    st.set(i, st.prod(l, r))

print(st.get(N+1) % 1000000007)