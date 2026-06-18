from math import atan2
N = int(input())
P = []
for _ in range(N):
    x, y = map(int,input().split())
    P.append((atan2(y,x),x,y))

P.sort()
ans = 0

for i in range(N):
    rad = P[i][0]
    sx, sy = 0, 0
    for j in range(N):
        nx, ny = P[(i+j)%N][1], P[(i+j)%N][2]
        if sx**2 + sy**2 < (sx+nx)**2 + (sy+ny)**2:
            sx += nx; sy += ny
    ans = max(ans, (sx**2 + sy**2)**(1/2))

print(ans)