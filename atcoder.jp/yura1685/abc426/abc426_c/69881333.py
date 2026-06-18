N, Q = map(int,input().split())

OS = [1] * N
A = 0

for _ in range(Q):
    X, Y = map(int,input().split())
    X, Y = X-1, Y-1
    cnt = 0
    for i in range(A,X+1):
        cnt += OS[i]
        OS[i] = 0
    OS[Y] += cnt
    print(cnt)
    if A <= X:
        A = X + 1