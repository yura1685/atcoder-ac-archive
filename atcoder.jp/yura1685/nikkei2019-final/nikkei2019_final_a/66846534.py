N = int(input())
A = list(map(int,input().split()))

for k in range(1,N+1):
    S = sum(A[:k])
    ans = S
    for i in range(N-k):
        S += A[k+i] - A[i]
        ans = max(ans,S)
    print(ans)