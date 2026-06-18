N, M = map(int, input().split())
S = [input() for _ in range(N)]
inf = float('inf')
go = [inf] * N
go[0] = 0
for i in range(N):
    for j in range(M):
        if S[i][j] == '1':
            go[i+j+1] = min(go[i+j+1], go[i] + 1)

co = [inf] * N
co[N-1] = 0
for i in range(N-1,-1,-1):
    for j in range(M):
        if S[i][j] == '1':
            co[i] = min(co[i], co[i+j+1] + 1)

ansL = []
for k in range(1, N-1):
    ans = inf
    for s in range(max(0, k-M+1),k):
        for i in range(M):
            if S[s][i] == '0':
                continue
            e = s + i + 1
            if e <= k:
                continue
            ans = min(ans, go[s] + 1 + co[e])
    ansL.append(ans if ans < inf else -1)

print(*ansL)