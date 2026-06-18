from collections import deque

a, N = map(int,input().split())

visited = set()
q = deque()
q.append((1,0))

while q:
    x, cnt = q.popleft()
    if x == N:
        print(cnt)
        break
    if x in visited:
        continue
    visited.add(x)

    ax = a*x
    if ax not in visited and ax < 10*N:
        q.append((ax, cnt+1))
    
    sx = str(x)
    if x >= 10 and sx[-1] != '0':
        rx = int(sx[-1]+sx[:-1])
        if rx not in visited:
            q.append((rx, cnt+1))

else:
    print(-1)