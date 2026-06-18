from bisect import bisect
from itertools import accumulate

N, Q = map(int,input().split())
R = list(map(int,input().split()))
R.sort()
R = list(accumulate(R))
for _ in range(Q):
    X = int(input())
    print(bisect(R,X))