from atcoder.fenwicktree import FenwickTree

N, Q = map(int, input().split())
fth = FenwickTree(Q + 1)
ftw = FenwickTree(Q + 1)
fth.add(0, N)
ftw.add(0, N)
th = [0] * N
tw = [0] * N
ans = 0

for t in range(1, Q + 1):
    q, x = map(int, input().split())
    x -= 1
    if q == 1:
        last = th[x]
        cnt = ftw.sum(0, last)
        ans += N - cnt
        fth.add(last, -1)
        th[x] = t
        fth.add(t, 1)
    else:
        last = tw[x]
        cnt = N - fth.sum(0, last + 1)
        ans -= cnt
        ftw.add(last, -1)
        tw[x] = t
        ftw.add(t, 1)
    print(ans)