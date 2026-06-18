K, M = map(int, input().split())
MOD = 10007 * M

def f(r, n, mod):
    res = 0
    sum = 1
    pow = r
    while n > 0:
        if n % 2 == 1:
            res = (res * pow + sum) % mod
        sum = sum * (1 + pow) % mod
        pow = pow ** 2 % mod
        n //= 2
    return res

ans = 0
for _ in range(K):
    c, l = map(int, input().split())
    hoge = c * f(10, l, MOD) % MOD
    ans = (ans * pow(10, l, MOD) + hoge) % MOD

print(ans // M)