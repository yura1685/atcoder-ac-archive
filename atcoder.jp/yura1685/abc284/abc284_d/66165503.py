from math import isqrt

def f(N):
    x = 2
    for p in range(2,isqrt(N//2)):
        if N % p == 0:
            x = p
            break
    N //= x
    if N % x == 0:
        y = N//x
        return x, y
    else:
        return isqrt(N), x
    
T = int(input())
for _ in range(T):
    n = int(input())
    print(*f(n))