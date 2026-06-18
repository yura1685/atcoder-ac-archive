from statistics import median_low

x, y = [], []
N = int(input())
for _ in range(N):
    X, Y = map(int,input().split())
    x.append(X); y.append(Y)

x.sort(); y.sort()

x_mid = median_low(x)
y_mid = median_low(y)

ans = 0
for i in range(N):
    ans += abs(x[i]-x_mid) + abs(y[i]-y_mid)

print(ans)