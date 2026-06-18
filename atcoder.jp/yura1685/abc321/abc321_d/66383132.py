from itertools import accumulate
from bisect import bisect

N, M, P = map(int,input().split())
A = list(map(int,input().split()))
B = list(map(int,input().split()))

A.sort()
B.sort()

sumB = [0] + list(accumulate(B))

money = 0

for a in A:
    c = bisect(B,P-a)
    money += sumB[c] + c*a + P*(M-c)

print(money)