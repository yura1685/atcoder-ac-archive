from math import isqrt

N = int(input())
ans = set()

for n in range(1,isqrt(N)+1):
    if N % n == 0:
        ans.add(n)
        ans.add(N//n)

for d in ans:
    print(d)