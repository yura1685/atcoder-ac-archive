N = int(input())
ans = N * (N + 1) * (N + 2) // 6
for _ in range(N-1):
    u, v = map(int, input().split())
    u, v = min(u, v), max(u, v)
    ans -= u * (N - v + 1)
print(ans)