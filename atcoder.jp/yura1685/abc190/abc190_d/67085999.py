from math import isqrt

N = int(input())
while N % 2 == 0:
    N //= 2

ans = 0
for i in range(1,isqrt(N)+1):
    if N % i == 0:
        ans += 2
if isqrt(N)**2 == N:
    ans -= 1

print(ans*2)