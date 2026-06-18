N, Q = map(int,input().split())
A = list(map(int,input().split()))
B = list(map(int,input().split()))

ans = sum(min(A[i],B[i]) for i in range(N))

for _ in range(Q):
    c, X, Y = input().split()
    X, Y = int(X)-1, int(Y)
    if c == 'A':
        if A[X] < B[X]:
            if Y <= A[X]:
                ans -= A[X] - Y
            elif A[X] < Y < B[X]:
                ans += Y - A[X]
            else:
                ans += B[X] - A[X]
        elif A[X] == B[X]:
            if Y < A[X]:
                ans -= A[X] - Y
        elif B[X] < A[X]:
            if Y <= B[X]:
                ans -= B[X] - Y            
        A[X] = Y
    else:
        if B[X] < A[X]:
            if Y <= B[X]:
                ans -= B[X] - Y
            elif B[X] < Y < A[X]:
                ans += Y - B[X]
            else:
                ans += A[X] - B[X]
        elif B[X] == A[X]:
            if Y < B[X]:
                ans -= B[X] - Y
        elif A[X] < B[X]:
            if Y <= A[X]:
                ans -= A[X] - Y
        B[X] = Y
    print(ans)