from atcoder.segtree import SegTree
from itertools import accumulate

N = int(input())
S = [0] + [1 if s == 'A' else -1 if s == 'B' else 0 for s in input()]
A = list(accumulate(S))

def op(x, y): return x + y

st = SegTree(op, 0, [0] * (2*N+10))

ans = 0
for a in A:
    ans += st.prod(0, a+N)
    st.set(a+N, st.get(a+N) + 1)
print(ans)