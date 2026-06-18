from more_itertools import run_length
from atcoder.segtree import SegTree

N, K = map(int, input().split())
S = input()
L = list(run_length.encode(S))
if S[0] == '0':
    L = [('1', 0)] + L
if S[-1] == '0':L.append(('1', 0))
L = [i for _, i in L]
def op(x, y): return x + y
st = SegTree(op, 0, L)
ans = 0
for i in range(0, len(L), 2):
    ans = max(ans, st.prod(i, min(len(L), i + 2*K + 1)))
print(ans)