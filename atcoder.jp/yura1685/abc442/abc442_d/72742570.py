from itertools import accumulate

N, Q = map(int,input().split())
A = [0] + list(map(int,input().split()))
S = list(accumulate(A))

for _ in range(Q):
    q = input().split()
    if q[0] == '1':
        x = int(q[1])
        S[x] += A[x+1] - A[x]
        A[x], A[x+1] = A[x+1], A[x]
    else:
        l, r = int(q[1]), int(q[2])
        print(S[r] - S[l-1])
