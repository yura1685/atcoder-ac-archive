def isqrt(n):
    l, r = 0, n
    while r - l > 1:
        mid = (l + r) // 2
        if mid * mid > n:
            r = mid
        else:
            l = mid
    return l

I = input().split()
L, R = int(I[0]), int(I[1])
if L == 1: L += 1
ans = 0

for x in range(L, R+1):
    primes = []
    N = x
    for p in range(2, isqrt(x+1) + 1):
        if N % p == 0:
            primes.append(p)
            while N % p == 0:
                N //= p
        if N == 1:
            break
    if N > 1: primes.append(N)
    res = 0
    M = len(primes)
    for i in range(1, 1 << M):
        n = 1
        bit_count = 0
        for j in range(M):
            if (i >> j) & 1:
                n *= primes[j]
                bit_count += 1
        res += (R // n - x // n) * pow(-1, bit_count + 1)
    res -= R // x - 1
    ans += res

print(2 * ans)