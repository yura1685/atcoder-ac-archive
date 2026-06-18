N, K = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]
D = [[N*N+1] * N for _ in range(N)]
for i in range(N):
    for j in range(N):
        if A[i][j] == 1: D[i][j] = 1
for j in range(N):
    for i in range(N):
        for k in range(N):
            D[i][k] = min(D[i][k], D[i][j] + D[j][k])

Q = int(input())
for _ in range(Q):
    u, v = map(int, input().split())
    u, v = u-1, v-1
    if A[u%N][v%N] == 1:
        print(1)
    else:
        if D[u%N][v%N] > N*N:
            print(-1)
        else:
            print(D[u%N][v%N])