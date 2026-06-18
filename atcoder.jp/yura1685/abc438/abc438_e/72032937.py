N, Q = map(int,input().split())
A = [0] + list(map(int,input().split()))
log = 60
to = [[0] * (N+1) for _ in range(60)]
sm = [[0] * (N+1) for _ in range(60)]

for i in range(1,N+1):
    to[0][i] = A[i]
    sm[0][i] = i

for k in range(59):
    for v in range(1, N+1):
        m = to[k][v]
        to[k+1][v] = to[k][m]
        sm[k+1][v] = sm[k][v] + sm[k][m]

for _ in range(Q):
    n, u = map(int,input().split())
    s = u
    ans = 0
    for k in range(60):
        if (n >> k) & 1:
            ans += sm[k][s]
            s = to[k][s]
    print(ans)