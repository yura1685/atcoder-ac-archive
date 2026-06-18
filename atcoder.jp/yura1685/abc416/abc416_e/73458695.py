N, M = map(int,input().split())

inf = float('inf')
D = [[inf]*(N+1) for _ in range(N+1)]
for i in range(N+1): D[i][i] = 0
for _ in range(M):
    A, B, C = map(int,input().split())
    if C < D[A][B]:
        D[A][B] = D[B][A] = C

_, T = map(int,input().split())
Air = list(map(int,input().split()))
for a in Air:
    D[a][0] = 0
    D[0][a] = T

for j in range(N+1):
    Dj = D[j]
    for i in range(N+1):
        Di = D[i]
        Dij = D[i][j]
        for k in range(N+1):
            if Di[k] > Dij + Dj[k]:
                Di[k] = Dij + Dj[k]

Q = int(input())
for _ in range(Q):
    q = list(map(int,input().split()))
    if q[0] == 1:
        x, y, t = q[1:]
        if D[x][y] <= t:
            continue
        Dx, Dy = D[x], D[y]
        Dx[y] = Dy[x] = t 
        for i in range(N+1):
            Di = D[i]
            Dix_t = Di[x] + t
            Diy_t = Di[y] + t
            for j in range(N+1):
                v1 = Dix_t + Dy[j]
                v2 = Diy_t + Dx[j]
                if v1 < Di[j]: Di[j] = v1
                if v2 < Di[j]: Di[j] = v2

    elif q[0] == 2:
        x = q[1]
        if D[x][0] == 0: continue
        D[x][0] = 0
        D[0][x] = T
        D0, Dx = D[0], D[x]
        for i in range(N+1):
            if D[i][x] < D[i][0]:
                D[i][0] = D[i][x]
            if T + Dx[i] < D0[i]:
                D0[i] = T + Dx[i]

        for i in range(N+1):
            Di = D[i]
            Di0 = Di[0]
            for j in range(N+1):
                if Di0 + D0[j] < Di[j]:
                    Di[j] = Di0 + D0[j]

    elif q[0] == 3:
        ans = 0
        for x in range(1,N+1):
            Dx = D[x]
            for y in range(x+1,N+1):
                if Dx[y] < inf:
                    ans += Dx[y]
        print(ans * 2)