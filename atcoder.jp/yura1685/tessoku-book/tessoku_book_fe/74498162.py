from bisect import bisect
from itertools import accumulate

N = int(input())
C = list(accumulate(sorted(map(int, input().split()))))

Q = int(input())
for _ in range(Q):
    X = int(input())
    print(bisect(C, X))