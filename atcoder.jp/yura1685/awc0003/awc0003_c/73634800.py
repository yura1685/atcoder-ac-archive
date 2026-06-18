N, K = map(int,input().split())
X = []
for _ in range(N):
    a, b = map(int,input().split())
    X.append((b-a, a, b))
X.sort()
ans = 0
for i in range(N):
    ans += X[i][2] if i < K else X[i][1]

print(ans)