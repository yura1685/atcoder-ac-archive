from itertools import accumulate

N, K = map(int,input().split())
A = list(map(int,input().split()))
if K % 2 == 0:
    print(sum(A[2*i+1] - A[2*i] for i in range(K//2)))
else:
    F = [0] + list(accumulate(A[i+1] - A[i] for i in range(0,K-1,2)))
    B = [0] + list(accumulate(A[i] - A[i-1] for i in range(K-1,0,-2)))
    B.reverse()
    ans = 10**10
    for i in range(K//2+1):
        ans = min(ans, F[i] + B[i])
    print(ans)