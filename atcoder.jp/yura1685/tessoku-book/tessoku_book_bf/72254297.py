from atcoder.segtree import SegTree

N, Q = map(int,input().split())

st = SegTree(max, -1, [0]*N)
for _ in range(Q):
    q, a, b = map(int,input().split())
    if q == 1:
        st.set(a-1, b)
    else:
        print(st.prod(a-1, b-1))