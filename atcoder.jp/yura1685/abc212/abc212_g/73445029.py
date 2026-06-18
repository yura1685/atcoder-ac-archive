P = int(input())
mod = 998244353

D = set()
p = 1
while p*p <= P-1:
    if (P-1) % p == 0:
        D.add(p)
        D.add((P-1)//p)
    p += 1
D = sorted(D)
N = len(D)
dp = [0] * N
for i in range(N-1,-1,-1):
    d = D[i]
    dp[i] = (P-1) // d 
    for j in range(i+1, N):
        if D[j] % D[i] == 0:
            dp[i] -= dp[j]

ans = 1
for i in range(N):
    ans += (P-1) // D[i] * dp[i]

print(ans % mod)