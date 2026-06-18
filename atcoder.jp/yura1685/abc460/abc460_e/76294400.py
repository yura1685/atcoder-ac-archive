from math import gcd
mod = 998244353

pow = [10 ** i for i in range(20)]

def solve():
    N, M = map(int, input().split())
    ans = 0
    for digit in range(1, 20):
        lo = pow[digit - 1]
        hi = min(N, pow[digit] - 1)
        y = 0 if lo > hi else hi - lo + 1
        if y == 0: continue
        g = gcd(pow[digit] - 1, M)
        ans = (ans + (N // (M // g)) * y) % mod
    print(ans)

for _ in range(int(input())):
    solve()