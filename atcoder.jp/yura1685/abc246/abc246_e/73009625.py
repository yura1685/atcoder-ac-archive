from collections import deque

N = int(input())
ax, ay = map(int,input().split())
bx, by = map(int,input().split())
ax, ay, bx, by = ax-1, ay-1, bx-1, by-1
inf = float('inf')
S = [input() for _ in range(N)]
A = [[inf]*N for _ in range(N)]
A[ax][ay] = 0
C = [(1,1),(1,-1),(-1,1),(-1,-1)]

dq = deque([(ax,ay)])
while dq:
    x, y = dq.popleft()
    for cx, cy in C:
        for d in range(1,N):
            nx, ny = x + cx*d, y + cy*d
            if not (0 <= nx < N and 0 <= ny < N):
                break
            if S[nx][ny] == '#':
                break
            if A[x][y] + 1 > A[nx][ny]:
                break
            if A[nx][ny] == inf:
                A[nx][ny] = A[x][y] + 1
                dq.append((nx,ny))

print(A[bx][by] if A[bx][by] < inf else -1)