X, Y, N = map(int,input().split())
if 3*X <= Y:
    print(X*N)
else:
    print(Y*(N//3)+X*(N%3))