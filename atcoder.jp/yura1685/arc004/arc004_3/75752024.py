from math import gcd
X, Y = map(int, input().split('/'))
g = gcd(X, Y)
X, Y = X // g, Y // g
ans = []
l, r = int(4*X / Y**2 - 2 / Y - 5), int(4*X / Y**2 + 2 / Y + 5)
for k in range(l, r+1):
    N = k * Y
    if N % 2: continue
    N //= 2
    M = N * (N+1) - k * X
    if M % 2: continue
    M //= 2
    if 1 <= M <= N and 2 * N * X == (N * (N+1) - 2*M) * Y:
        ans.append((N, M))
ans.sort()
if ans:
    for n, m in ans:
        print(n, m)
else:
    print('Impossible')