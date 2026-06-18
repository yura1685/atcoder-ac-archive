from atcoder.segtree import SegTree

N, Q = map(int, input().split())
A = list(map(int, input().split()))
K = 5 * 10 ** 5 + 1
cnt = [0] * K
sum = [0] * K
for a in A: cnt[a] += 1
for a in A: sum[a] += a 
def op(x, y): return x + y 
st_cnt = SegTree(op, 0, cnt)
st_sum = SegTree(op, 0, sum)

for _ in range(Q):
    q, x, y = map(int, input().split())
    if q == 1:
        n = A[x-1]
        A[x-1] = y
        st_cnt.set(n, st_cnt.get(n) - 1)
        st_cnt.set(y, st_cnt.get(y) + 1)
        st_sum.set(n, st_sum.get(n) - n)
        st_sum.set(y, st_sum.get(y) + y)
    else:
        if x > y:
            ans = x * N
        else:
            ans = x * st_cnt.prod(0, x) + st_sum.prod(x, y+1) + y * st_cnt.prod(y+1, K)
        print(ans)