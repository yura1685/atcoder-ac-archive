N, M, D = map(int, input().split())
T = list(map(int, input().split()))
ans = 0
for t in T:
    if t <= M:
        pass
    else:
        ans += (t - M + D - 1) // D
print(ans)