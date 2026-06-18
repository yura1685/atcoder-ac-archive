N, Q = map(int, input().split())
up = [-1] * N
do = [-1] * N
for _ in range(Q):
    C, P = map(int, input().split())
    C, P = C-1, P-1
    if do[C] != -1:
        n = do[C]
        up[n] = -1
    do[C] = P
    up[P] = C

ans = []
for i in range(N):
    if do[i] != -1:
        ans.append(0)
    else:
        cnt = 0
        now = i
        while now != -1:
            now = up[now]
            cnt += 1
        ans.append(cnt)

print(*ans)