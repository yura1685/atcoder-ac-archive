from collections import defaultdict

N = int(input())
X, Y = [], []
for i in range(N):
    x, y = map(int, input().split())
    X.append((x, i))
    Y.append((y, i))

X.sort()
Y.sort()

ans = sorted([(X[N-1][0] - X[0][0], X[N-1][1] * N + X[0][1]),
              (X[N-1][0] - X[1][0], X[N-1][1] * N + X[1][1]),
              (X[N-2][0] - X[0][0], X[N-2][1] * N + X[0][1]),
              (Y[N-1][0] - Y[0][0], Y[N-1][1] * N + Y[0][1]),
              (Y[N-1][0] - Y[1][0], Y[N-1][1] * N + Y[1][1]),
              (Y[N-2][0] - Y[0][0], Y[N-2][1] * N + Y[0][1])],
              reverse=True)

print(ans[1][0] if ans[1][1] != ans[0][1] else ans[2][0])