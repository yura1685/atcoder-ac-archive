from atcoder.segtree import SegTree

N, M, K = map(int, input().split())
A = [int(x) for x in input().split()]
V = [(0, 0) for _ in range(N + 1)]
for a in A: V[a] = (0, 1)
def op(x, y): return (x[0] + y[0], x[1] + y[1])
S = SegTree(op, (0, 0), V)

for i in range(N-1, -1, -1):
    if S.get(i)[1] == 1: continue
    x, y = S.prod(i + 1, min(N + 1, i + M + 1))
    S.set(i, (x / M + 1, y / M))

x, y = S.get(0)
print(-1 if abs(1-y) < 1e-8 else x / (1 - y))