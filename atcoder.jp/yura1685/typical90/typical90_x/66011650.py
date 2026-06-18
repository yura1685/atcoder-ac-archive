N, K = map(int,input().split())
A = list(map(int,input().split()))
B =list(map(int,input().split()))

dis = 0
for i in range(N):
    dis += abs(A[i]-B[i])

if K < dis:
    print('No')
else:
    if (K-dis) % 2 == 0:
        print('Yes')
    else:
        print('No')