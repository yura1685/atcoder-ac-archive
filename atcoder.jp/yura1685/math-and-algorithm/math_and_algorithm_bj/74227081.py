N = int(input())
X, Y = [], []
for _ in range(N):
    x, y = map(int, input().split())
    X.append(x)
    Y.append(y)
X.sort()
Y.sort()
ans = 0
for i in range(N):
    ans += (X[i] + Y[i]) * (2*i + 1 - N)
print(ans)