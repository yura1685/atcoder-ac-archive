from collections import deque

N = int(input())
G = [[0]*N for _ in range(N)]
d = deque([(0,(N-1)//2)])
G[0][(N-1)//2] = 1
for _ in range(N*N-1):
    r, c = d.popleft()
    k = G[r][c]
    if G[(r-1)%N][(c+1)%N] == 0:
        G[(r-1)%N][(c+1)%N] = k+1
        d.append(((r-1)%N,(c+1)%N))
    else:
        G[(r+1)%N][c] = k+1
        d.append(((r+1)%N,c))

for g in G:
    print(*g)