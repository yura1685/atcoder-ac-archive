N = int(input())
A = list(map(int,input().split()))

ans = 0
for i in range(N):
    m = A[i]
    x = 0
    for j in range(i,N):
        m = min(m, A[j])
        x = max(x, (j-i+1)*m)
    ans = max(ans, x)

print(ans)