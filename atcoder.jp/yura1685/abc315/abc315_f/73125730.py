from functools import cache

N = int(input())
P = []
for _ in range(N):
    X, Y = map(int,input().split())
    P.append((X,Y))

inf = float('inf')
dp = [[inf] * 30 for _ in range(N)]
dp[0][0] = 0

@cache
def dist(i,j):
    xi, yi = P[i]
    xj, yj = P[j]
    return ((xi-xj)**2 + (yi-yj)**2)**(1/2)

for i in range(1,N):
    for c in range(30):
        for j in range(i-1,-1,-1):
            skip = i-j-1
            if skip > c:
                break
            dp[i][c] = min(dp[i][c], dp[j][c-skip] + dist(j,i))

ans = dp[-1][0]
for c, w in enumerate(dp[-1]):
    if c == 0:
        continue
    ans = min(ans, w + 2**(c-1))

print(ans)