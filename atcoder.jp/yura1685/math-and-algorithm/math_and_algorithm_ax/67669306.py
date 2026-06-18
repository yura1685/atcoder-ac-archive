N, X, Y = map(int,input().split())
if abs(X+Y) <= N and (X+Y) % 2 == N % 2:
    print('Yes')
else:
    print('No')