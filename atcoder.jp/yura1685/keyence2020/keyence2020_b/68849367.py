N = int(input())
robot = []
for _ in range(N):
    X, Li = map(int,input().split())
    L, R = (X-Li)*2, (X+Li)*2-1
    robot.append((R,L))
robot.sort()
I = float('INF')
l, r = -I, -I
ans = 0
for R, L in robot:
    if max(l,L) > min(r,R):
        l, r = L, R
        ans += 1
print(ans)