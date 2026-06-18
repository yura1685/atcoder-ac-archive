from math import isqrt

N = int(input())
ans = 1685168516851685
for a in range(1, isqrt(N) + 1):
    if N % a == 0:
        b = N // a
        ans = min(2 * (a + b), ans)
print(ans)