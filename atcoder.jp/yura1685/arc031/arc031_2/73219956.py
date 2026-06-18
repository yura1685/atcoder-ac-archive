from collections import deque

N = 10
C = [input() for _ in range(N)]
c = [(-1,0),(0,-1),(0,1),(1,0)]

isl = 0
sx, sy = -1, -1
for i in range(N):
    for j in range(N):
        if C[i][j] == 'o':
            isl += 1

for i in range(N):
    for j in range(N):
        if C[i][j] == 'o':
            continue
        cnt = 0
        check = [[0]*N for _ in range(N)]
        check[i][j] = 1
        dq = deque([(i,j)])
        while dq:
            x, y = dq.popleft()
            for dx, dy in c:
                nx, ny = x + dx, y + dy
                if not (0 <= nx < N and 0 <= ny < N):
                    continue
                if check[nx][ny] == 1 or C[nx][ny] == 'x':
                    continue
                check[nx][ny] = 1
                dq.append((nx,ny))
                cnt += 1

        if cnt == isl:
            exit(print('YES'))

print('NO')