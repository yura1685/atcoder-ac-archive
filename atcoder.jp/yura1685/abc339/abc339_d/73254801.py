from collections import deque

N = int(input())
S = [input() for _ in range(N)]
P = []
for i in range(N):
    for j in range(N):
        if S[i][j] == 'P':
            P.append(i)
            P.append(j)

x1, y1, x2, y2 = P
inf = float('inf')
step = [[[[inf]*N for _ in range(N)] for _ in range(N)] for _ in range(N)]
step[x1][y1][x2][y2] = 0
c = [(-1,0),(0,-1),(0,1),(1,0)]
L = [-1,N]
dq = deque([(x1,y1,x2,y2)])

while dq:
    x1, y1, x2, y2 = dq.popleft()
    if (x1, y1) == (x2, y2):
        exit(print(step[x1][y1][x2][y2]))
    for dx, dy in c:
        nx1, ny1, nx2, ny2 = x1+dx, y1+dy, x2+dx, y2+dy
        if nx1 in L or ny1 in L or S[nx1][ny1] == '#':
            nx1, ny1 = x1, y1
        if nx2 in L or ny2 in L or S[nx2][ny2] == '#':
            nx2, ny2 = x2, y2  
        if step[x1][y1][x2][y2] + 1 >= step[nx1][ny1][nx2][ny2]:
            continue
        step[nx1][ny1][nx2][ny2] = step[x1][y1][x2][y2] + 1
        dq.append((nx1,ny1,nx2,ny2))

print(-1)