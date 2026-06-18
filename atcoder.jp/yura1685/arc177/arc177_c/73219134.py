from collections import deque

N = int(input())
C = [input() for _ in range(N)]
c = [(-1,0),(0,-1),(0,1),(1,0)]

ans = 0

check = [[0]*N for _ in range(N)]
check[0][0] = 1
dq = deque([(0,0,0)])
while dq:
    x, y, step = dq.popleft()
    if (x, y) == (N-1, N-1):
        ans += step
        break
    for dx, dy in c:
        nx, ny = x + dx, y + dy
        if not (0 <= nx < N and 0 <= ny < N):
            continue
        if check[nx][ny] == 0:
            check[nx][ny] = 1
            if C[nx][ny] == 'R':
                dq.appendleft((nx,ny,step))
            else:
                dq.append((nx,ny,step+1))

check = [[0]*N for _ in range(N)]
check[0][N-1] = 1
dq = deque([(0,N-1,0)])
while dq:
    x, y, step = dq.popleft()
    if (x, y) == (N-1, 0):
        ans += step
        break
    for dx, dy in c:
        nx, ny = x + dx, y + dy
        if not (0 <= nx < N and 0 <= ny < N):
            continue
        if check[nx][ny] == 0:
            check[nx][ny] = 1
            if C[nx][ny] == 'B':
                dq.appendleft((nx,ny,step))
            else:
                dq.append((nx,ny,step+1))

print(ans)