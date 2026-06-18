N, X = map(int, input().split())
ans = 0
for a in range(1, N+1):
    for b in range(a+1, N+1):
        for c in range(b+1, N+1):
            if a + b + c == X:
                ans += 1
print(ans)