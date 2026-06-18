from itertools import accumulate

N, Q = map(int,input().split())
A = [0] + list(map(int,input().split()))
B = list(accumulate(A))
c = 0

for _ in range(Q):
    q = list(map(int,input().split()))
    if q[0] == 1:
        c += q[1]
        c %= N
    else:
        l, r = q[1:]
        l, r = (l+c-1) % N + 1, (r+c-1) % N + 1
        if l <= r:
            print(B[r] - B[l-1])
        else:
            print(B[r] + B[N] - B[l-1])
        