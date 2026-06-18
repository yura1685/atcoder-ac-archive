from atcoder.fenwicktree import FenwickTree

N, Q = map(int, input().split())
L = [0] * N
line = 0
cnt = FenwickTree(2 * Q + 10)
cnt.add(0, N)
now = 0
for _ in range(Q):
    i, t = map(int, input().split())
    if i == 1:
        p = L[t-1]
        cnt.add(L[t-1], -1)
        L[t-1] += 1
        cnt.add(L[t-1], 1)
        if p == now and cnt.sum(now, now + 1) == 0:
            line += 1
            now += 1
    else:
        if t + line > Q:
            print(0)
        else:
            print(cnt.sum(t + line, 2 * Q + 5))