from atcoder.lazysegtree import LazySegTree
from sortedcontainers import SortedList

N, M = map(int, input().split())
C = [[] for _ in range(M+1)]
for _ in range(N):
    A, B = map(int, input().split())
    C[A].append(-1)
    C[B].append(A)

S1, S2 = SortedList(), SortedList()
cnt = 0
def op(a, b): return min(a, b)
_e = 1<<60
def mapp(f, x): return f+x
def comp(f, g): return f+g
lst = LazySegTree(op, _e, mapp, comp, 0, [0] * (M+1))

for i, cl in enumerate(C):
    if i == 0: continue
    for c in cl:
        if c == -1:
            cnt += 1
            S1.add(i)
        if c > 0:
            S2.add(c)
            S1.discard(c)
            S1.add(i)
    if cnt < N:
        continue
    Max = S1[0]
    lst.apply(i-Max+1, i+1, 1)

ans = [lst.get(i) for i in range(1, M+1)]
print(*ans)