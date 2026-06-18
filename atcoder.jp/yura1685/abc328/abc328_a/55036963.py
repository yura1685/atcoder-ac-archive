N, X = map(int, input().split())
L = list(map(int, input().split()))
ans = 0
for i in range(N):
    if L[i] <= X:
        ans += L[i]
print(ans)