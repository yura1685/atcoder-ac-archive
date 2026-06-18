a1 = list(map(int,input().split()))
a2 = list(map(int,input().split()))
a3 = list(map(int,input().split()))

A = a1 + a2 + a3

N = int(input())
for _ in range(N):
    b = int(input())
    if b in A:
        A[A.index(b)] = 0

if A[:3] == [0,0,0] or A[3:6] == [0,0,0] or A[6:] == [0,0,0]:
    print('Yes')
elif A[0] == A[3] == A[6] == 0 or A[1] == A[4] == A[7] == 0 or A[2] == A[5] == A[8] == 0:
    print('Yes')
elif A[0] == A[4] == A[8] == 0 or A[2] == A[4] == A[6] == 0:
    print('Yes')
else:
    print('No')