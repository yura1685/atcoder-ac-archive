N, D = map(int, input().split())
mod = 998244353
ans = 0
for d in range(N - 1):
    a = pow(2, D+1, mod) if d + D < N else 0
    b = 0 if (2*(N-1-d) < D or D == 1) else pow(2, D-1, mod) * (D-1) if d + D < N else pow(2, D-1, mod) * (2*N - 2*d - D - 1)
    ans += pow(2, d, mod) * (a + b) % mod
print(ans % mod)