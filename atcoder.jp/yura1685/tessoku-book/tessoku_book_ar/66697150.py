N, Q = map(int,input().split())
A = [i for i in range(N+1)]
rev = 0

for _ in range(Q):
    c = list(map(int,input().split()))
    if c[0] == 1:
        if rev:
            A[N-c[1]+1] = c[2]
        else:
            A[c[1]] = c[2]
    elif c[0] == 2:
        rev = 1-rev
    else:
        if rev:
            print(A[N-c[1]+1])
        else:
            print(A[c[1]])