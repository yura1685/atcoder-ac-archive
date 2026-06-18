K = int(input())
mod = 998244353
ans = 0
for x in range(2, K):
    for y in range(2, K):
        z = K - x - y
        if z < 2:
            continue
        ans += (x-1) * (y-1) * (z-1) * (K - max(x,y,z)) % mod
        ans %= mod

print(ans)