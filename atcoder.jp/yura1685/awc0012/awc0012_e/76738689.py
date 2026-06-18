from atcoder.segtree import SegTree

inf = 10 ** 18
N, K = map(int, input().split())
A = list(map(int, input().split()))
dp = SegTree(max, -inf, [-inf]*N)
dp.set(0, A[0])
for i, a in enumerate(A):
    if i == 0:
        continue
    dp.set(i, dp.prod(max(0, i-K), i+1) + a)
print(dp.get(N-1))