D, N = map(int,input().split())
mod = 998244353
M = N - D
if M == 1 or M < 0: exit(print(0))
ans = 0

f = [1]
for i in range(1,D+1):
    x = f[-1] * i % mod
    f.append(x)
finv = [pow(a,mod-2,mod) for a in f]

def comb(k):
    return f[D] * finv[k] * finv[D-k] % mod

for s in range(D+1):
    x = M - 3*s
    if x < 0: break
    if x % 2 == 0:
        t = x//2
        if t <= D:
            ans += comb(s) * comb(t)
            ans %= mod
print(ans)