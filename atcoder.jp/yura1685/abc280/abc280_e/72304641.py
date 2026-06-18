N, P = map(int,input().split())
mod = 998244353
p = P*pow(100,-1,mod)%mod
q = (1-p) % mod
dp = [1, (p+2*q)%mod]
for i in range(N-2):
    x = (1 + dp[-2])*p + (1+dp[-1])*q
    dp.append(x%mod)

print(dp[N-1])