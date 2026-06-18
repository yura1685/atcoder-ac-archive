from collections import defaultdict
from itertools import accumulate
from bisect import *

N, M = map(int, input().split())
A = list(map(int, input().split()))
cnt = defaultdict(int)
depth = [[] for _ in range(N)]

for a in A:
    cnt[a] += 1
    dep = cnt[a]
    depth[dep-1].append(a)

for d in depth: d.sort()
nokori = [M - len(d) for d in depth]
nokori_ac = list(accumulate(nokori))
# print(depth)
# print(nokori, nokori_ac)

Q = int(input())
for _ in range(Q):
    X = int(input())
    if X <= N:
        print(A[X - 1])
    else:
        X -= N
        dep = bisect_left(nokori_ac, X)
        if dep < N:
            L = depth[dep]
            if dep > 0: X -= nokori_ac[dep-1]
            if not L:
                print(X)
            else:
                l, r = 0, len(L) - 1
                if X <= L[0] - 1:
                    print(X)
                elif X > L[r] - (r+1):
                    print(X + len(L))
                else:
                    while l < r:
                        mid = (l + r) // 2
                        miss = L[mid] - (mid + 1)
                        if miss < X:
                            l = mid + 1
                        else:
                            r = mid
                    print(X + l)
        else:
            X -= nokori_ac[N-1]
            print((X-1) % M + 1)