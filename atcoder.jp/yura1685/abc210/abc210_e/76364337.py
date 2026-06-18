from math import gcd

N, M = map(int, input().split())
E = [tuple(map(int, input().split())) for _ in range(M)]
E.sort(key=lambda x: x[1])

g = N
X = [N]
for a, c in E:
    g = gcd(g, a)
    X.append(g)

if X[-1] > 1:
    print(-1)

else:
    ans = 0
    for i in range(M):
        ans += E[i][1] * (X[i] - X[i+1])
    print(ans)