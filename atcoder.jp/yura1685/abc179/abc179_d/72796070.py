from atcoder.lazysegtree import LazySegTree
mod = 998244353
def plus(x,y): return (x + y) % mod

N, K = map(int,input().split())
S = sorted(tuple(map(int,input().split())) for _ in range(K))
J = [0]*N; J[0] = 1
LST = LazySegTree(max, -1, plus, plus, 0, J)

for i in range(N-1):
    now = LST.get(i)
    for x, y in S:
        l, r = i + x, i + y
        if l >= N:
            break
        if r >= N:
            r = N-1
        LST.apply(l,r+1,now)

print(LST.get(N-1) % mod)