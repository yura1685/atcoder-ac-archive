N, M = map(int,input().split())
ans = 0

for bit in range(61):
    if (M >> bit) & 1 == 0:
        continue
    X, Y = N // (1 << bit+1), N % (1 << bit+1)
    cnt = X * (1 << bit) + max(0, Y - (1 << bit) + 1)
    ans += cnt

print(ans % 998244353)