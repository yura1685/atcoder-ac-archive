from math import isqrt

N = int(input())

n = 1
while 2**n <= N:
    n += 1
n -= 1

ans = 0
for i in range(1,n+1):
    b = isqrt(N // (2**i))
    ans += (b+1) // 2

print(ans)