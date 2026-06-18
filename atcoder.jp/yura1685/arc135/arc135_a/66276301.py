from functools import cache
MOD = 998244353
X = int(input())

@cache
def f(n):
    if n <= 4:
        return n
    return f(n//2)*f(-(-n//2)) % MOD

print(f(X))