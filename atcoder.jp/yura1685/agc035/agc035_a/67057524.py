N = int(input())
A = list(map(int,input().split()))
A.sort()

if N % 3 != 0:
    if A[-1] == 0:
        print('Yes')
    else:
        print('No')
    exit()

if A[0] == A[N//3-1] and A[N//3] == A[2*N//3-1] and A[2*N//3] == A[N-1]:
    if len(set([A[0],A[N//3],A[2*N//3]])) == 3 and A[0]^A[N//3]^A[2*N//3]==0:
        print('Yes')
        exit()
    elif [A[0],A[N//3],A[2*N//3]].count(0) in [1,3]:
        print('Yes')
        exit()
print('No')