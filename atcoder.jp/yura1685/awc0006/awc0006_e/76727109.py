from atcoder.segtree import SegTree

N, Q = map(int, input().split())
S = list(map(int, input().split()))
def op(x, y): return x + y
st = SegTree(op, 0, S)
for _ in range(Q):
    q, a, b = map(int, input().split())
    if q == 1:
        print(st.prod(a-1, b))
    else:
        st.set(a-1, b)