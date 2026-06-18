N, K, L = map(int, input().split())
mod = 998244353

ans = 1
for i in range(N):
    if i < N - K:
        ans *= (L - i)
    else:
        ans *= (L - N + K)
    ans %= mod

print(ans)