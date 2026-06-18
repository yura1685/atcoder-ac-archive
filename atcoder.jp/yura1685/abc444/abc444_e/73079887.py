from atcoder.fenwicktree import FenwickTree
from bisect import bisect_left, bisect_right

N, D = map(int,input().split())
A = list(map(int,input().split()))
B = sorted(set(A))
d = {v:i for i, v in enumerate(B)}
FT = FenwickTree(len(B)+1)

ans = 0
l = 0

for r in range(N):
    bl = bisect_right(B, A[r] - D)
    br = bisect_left(B, A[r] + D)
    while FT.sum(bl, br) > 0:
        FT.add(d[A[l]], -1)
        l += 1
    FT.add(d[A[r]], 1)
    ans += r - l + 1

print(ans)