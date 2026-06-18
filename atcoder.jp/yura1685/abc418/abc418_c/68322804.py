from bisect import *
from itertools import accumulate

N, Q = map(int,input().split())
A = sorted(map(int,input().split()))
AC = list(accumulate(A))

for _ in range(Q):
    B = int(input())
    if A[-1] < B:
        print(-1)
        continue
    ans = 0
    ind = bisect_left(A,B-1)
    ans += AC[ind-1] if ind else 0
    ans += (N-ind)*(B-1) + 1
    print(ans)