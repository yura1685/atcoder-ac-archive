from itertools import permutations

N, M, R = map(int,input().split())
r = [int(x)-1 for x in input().split()]
INF = float('inf')
G = [[INF if i != j else 0 for j in range(N)] for i in range(N)]
for _ in range(M):
    a, b, c = map(int,input().split())
    G[a-1][b-1] = c
    G[b-1][a-1] = c

for k in range(N):
    for i in range(N):
        for j in range(N):
            G[i][j] = min(G[i][j], G[i][k]+G[k][j])
            G[j][i] = min(G[j][i], G[j][k]+G[k][i])

ans = INF
for P in permutations(r):
    dis = 0
    for i in range(R-1):
        dis += G[P[i]][P[i+1]]
    if dis < ans:
        ans = dis
        
print(ans)