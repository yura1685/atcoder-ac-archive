from math import isqrt

N = int(input())

for n in range(2,isqrt(N)+1):
    if N % n == 0:
        print('No')
        exit()
print('Yes')