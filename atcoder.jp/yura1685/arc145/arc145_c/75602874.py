N = int(input())
mod = 998244353
fac = [1]
for i in range(1,2*N+1):
    fac.append(fac[-1] * i % mod)
ans = pow(2, N, mod) * fac[2*N] * pow(fac[N+1], -1, mod) % mod
print(ans)