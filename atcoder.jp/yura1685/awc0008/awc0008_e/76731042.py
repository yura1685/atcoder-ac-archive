from atcoder.segtree import SegTree

N = int(input())
def op(x, y): return x + y
st = SegTree(op, 0, [0] * (N+1))
A = list(map(int, input().split()))
ans = 0
for a in A:
    ans += st.prod(a, N+1)
    st.set(a, 1)
print(ans)