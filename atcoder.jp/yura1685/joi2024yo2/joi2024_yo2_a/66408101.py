N = int(input())
A = list(set(map(int,input().split())))
A.sort()
N = len(A)
for i in range(N):
    if i <= N-7:
        c = A[i+1:i+7]
    else:
        c = A[i+1:]
    if A[i]+3 in c and A[i]+6 in c:
        print('Yes')
        exit()
print('No')