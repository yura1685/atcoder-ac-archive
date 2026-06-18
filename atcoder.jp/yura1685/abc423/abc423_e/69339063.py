from itertools import accumulate

N, Q = map(int,input().split())
A = list(map(int,input().split()))
B = [(i+1)*A[i] for i in range(N)]
C = [(i+1)**2*A[i] for i in range(N)]

SA = [0] + list(accumulate(A))
SB = [0] + list(accumulate(B))
SC = [0] + list(accumulate(C))

for _ in range(Q):
    L, R = map(int,input().split())
    a = SA[R] - SA[L-1]
    b = SB[R] - SB[L-1]
    c = SC[R] - SC[L-1]
    # print(a,b,c)
    print((-R*L+R-L+1)*a + (R+L)*b - c)