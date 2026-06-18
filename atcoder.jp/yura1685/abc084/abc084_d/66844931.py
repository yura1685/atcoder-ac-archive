from math import isqrt
from bisect import *

prime = []
like2017 = []

for n in range(2,10**5+1):
    for p in range(2,isqrt(n)+1):
        if n % p == 0:
            break
    else:
        prime.append(n)
        if n % 2 == 1 and (n+1)//2 in prime:
            like2017.append(n)

Q = int(input())
for _ in range(Q):
    l, r = map(int,input().split())
    print(bisect(like2017,r) - bisect_left(like2017,l))