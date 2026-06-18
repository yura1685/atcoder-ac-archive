N = int(input())
S = input()
LCP = [[0]*(N+1) for _ in range(N+1)]

for i in range(N-1,-1,-1):
    for j in range(N-1,-1,-1):
        if S[i] == S[j]:
            LCP[i][j] = 1 + LCP[i+1][j+1]

ans = 0
for i in range(N):
    for j in range(i+1,N):
        ans = max(ans, min(LCP[i][j], j-i))

print(ans)