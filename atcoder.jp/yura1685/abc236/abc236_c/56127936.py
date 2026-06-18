N, M = map(int,input().split())
A = list(map(str,input().split()))
B = list(map(str,input().split()))

a = 0

for i in range(N):
    if A[i] == B[a]:
        print('Yes')
        a += 1
    else:
        print('No')