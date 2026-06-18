from random import randint
from math import isqrt
from collections import Counter

N = int(input())
A = list(map(int,input().split()))
s = set()

for _ in range(200):
    i = randint(0,N-1)
    j = randint(0,N-1)
    if i == j:
        j = (j+1) % N
    X = abs(A[i] - A[j])
    for k in range(1,isqrt(X)+1):
        if X % k == 0:
            if k >= 3: s.add(k)
            if X//k >= 3: s.add(X//k)

for m in s:
    Am = [a % m for a in A]
    y = max(Counter(Am).values())
    if 2*y > N:
        exit(print(m))

print(-1)