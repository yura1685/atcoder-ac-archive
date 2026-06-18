from math import isqrt

N = int(input())
rN = isqrt(N)

if rN ** 2 == N:
    print(0)
else:
    print((rN+1)**2 - N)