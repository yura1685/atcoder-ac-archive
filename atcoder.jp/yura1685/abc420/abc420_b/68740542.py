N, M = map(int,input().split())
S = [input() for _ in range(N)]
ans = [0]*N

for j in range(M):
    x, y = 0, 0
    for i in range(N):
        if S[i][j] == '0':
            x += 1
        else:
            y += 1
    p = ''
    if y == 0 or x < y:
        p = '0'
    if x == 0 or y < x:
        p = '1'
    for i in range(N):
        if S[i][j] == p:
            ans[i] += 1

m = max(ans)
print(*[i+1 for i in range(N) if ans[i] == m])