N, L, R = map(int, input().split())
ans = 0
for bit in range(60):
    if N & (1 << bit):
        x, y = 1 << bit, 1 << (bit + 1)
        ans += max(0, min(R + 1, y) - max(L, x))
print(ans)