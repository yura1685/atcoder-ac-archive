from math import isqrt

def solve():
    N = int(input())
    ans = 0
    mod = 998244353
    for y in range(1, isqrt(N)+1):
        ans += 6 * (y-1) * (N // y - y)
        ans += 3 * (N // y - y)
        ans += 3 * (y - 1)
        ans += 1
        ans %= mod
    print(ans)

t = int(input())
for _ in range(t):
    solve()