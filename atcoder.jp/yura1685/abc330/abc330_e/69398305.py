from collections import defaultdict
from sortedcontainers import SortedList

N, Q = map(int,input().split())
A = list(map(int,input().split()))
sl = SortedList([i for i in range(N+10)])
d = defaultdict(int)
for a in A:
    d[a] += 1
    sl.discard(a)

for _ in range(Q):
    i, x = map(int,input().split())
    i -= 1
    a = A[i]
    A[i] = x
    d[a] -= 1
    if d[a] == 0:
        sl.add(a)
    d[x] += 1
    if d[x] == 1:
        sl.discard(x)
    print(sl[0])