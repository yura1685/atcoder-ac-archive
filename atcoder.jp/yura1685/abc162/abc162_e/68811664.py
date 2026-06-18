N, K = map(int,input().split())
mod = 10**9 + 7

G = [0]*(K+1) # G[g]: gcd がちょうどgであるものの総数
for g in range(K,0,-1):
    n = pow(K//g, N, mod)
    for i in range(2*g,K+1,g):
        n -= G[i]
    G[g] = n

ans = 0
for i in range(K+1):
    ans += i * G[i]
    ans %= mod

print(ans)