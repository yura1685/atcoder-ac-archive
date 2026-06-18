from atcoder.segtree import SegTree

N, D = map(int,input().split())
A = list(map(int,input().split()))
MA = max(A)
dp = SegTree(max, 0, [0]*(MA+1))

for a in A:
    l, r = max(0, a-D), min(MA,a+D)+1
    M = dp.prod(l, r)
    dp.set(a, M+1)

print(dp.all_prod())