N = int(input())
ans = 0
for k in range(1, 20):
    Rep = (10 ** k - 1) // 9
    for d in range(20):
        L = Rep * 10 ** d
        R = (Rep + 1) * 10 ** d - 1
        ans += max(0, min(R, N) - L + 1)
print(ans)