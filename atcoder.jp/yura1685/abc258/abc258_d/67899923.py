N, X = map(int,input().split())

ans = float('inf')
S = 0
for i in range(N):
    A, B = map(int,input().split())
    S += A+B
    ans = min(ans,S+max(0,B*(X-i-1)))

print(ans)