def axmod(a, x, m):
    result = 1
    a = a % m
    while x > 0:
        if x % 2 == 1:
            result = (result * a) % m
        a = (a * a) % m
        x //= 2
    return result

N, K = map(int,input().split())
MOD = 10**9+7
ans = K
if N == 1:
    print(ans)
    exit()

ans *= K-1
if N != 2:
    ans *= axmod(K-2,N-2,MOD)

print(ans % MOD)