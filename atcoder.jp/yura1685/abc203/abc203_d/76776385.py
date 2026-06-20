N, K = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]

ng, ok = -1, 10 ** 9
while ok - ng > 1:
    mid = (ng + ok) // 2
    S = [[0] * (N + 1) for _ in range(N + 1)]
    for i in range(N):
        for j in range(N):
            if A[i][j] <= mid:
                S[i+1][j+1] = 1
    for i in range(1, N+1):
        for j in range(1, N+1):
            S[i][j] += S[i-1][j] + S[i][j-1] - S[i-1][j-1]
    flag = False
    for i in range(1, N-K+2):
        for j in range(1, N-K+2):
            cnt = S[i+K-1][j+K-1] - S[i+K-1][j-1] - S[i-1][j+K-1] + S[i-1][j-1]
            if cnt >= (K ** 2 + 1) // 2:
                flag = True
                break
        if flag:
            break
    if flag:
        ok = mid
    else:
        ng = mid

print(ok)