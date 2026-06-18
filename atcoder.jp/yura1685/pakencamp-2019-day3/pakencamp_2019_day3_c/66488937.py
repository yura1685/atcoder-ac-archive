N, M = map(int,input().split())
A = [list(map(int,input().split())) for _ in range(N)]

ans = 0
for i in range(M-1):
    for j in range(i+1,M):
        score = sum([max(A[c][i],A[c][j]) for c in range(N)])
        ans = max(ans,score)

print(ans)