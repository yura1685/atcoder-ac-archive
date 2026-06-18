N = int(input())
d = dict()
for _ in range(N):
    S, D = input().split()
    d[S] = int(D)
Q = int(input())
for _ in range(Q):
    X, Y = input().split()
    print(abs(d[X] - d[Y]))