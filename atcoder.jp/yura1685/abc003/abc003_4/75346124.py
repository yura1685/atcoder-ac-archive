def fact(n):
    res = 1
    for i in range(1, n+1):
        res = res * i % mod
    return res

def comb(n, k):
    if n < k: return 0
    return fact(n) * pow(fact(k), -1, mod) * pow(fact(n-k), -1, mod)

mod = 10 ** 9 + 7
H, W = map(int, input().split())
X, Y = map(int, input().split())
D, L = map(int, input().split())
DL = D + L
ans = comb(X*Y, DL) - 2 * (comb(X*(Y-1), DL) + comb((X-1)*Y, DL)) + (4*comb((X-1)*(Y-1), DL) + comb((X-2)*Y, DL) + comb(X*(Y-2), DL)) - 2*(comb((X-1)*(Y-2), DL) + comb((X-2)*(Y-1), DL)) + (comb((X-2)*(Y-2), DL) if X + Y > 2 else 0)
ans %= mod
print(ans * comb(DL, D) * (H-X+1) * (W-Y+1) % mod)