N = int(input())
X = list(map(int,input().split()))
Y = sorted(X)

c = Y[N//2-1]

for i in range(0,N):
    if X[i] <= c:
        print(Y[N//2])
    else:
        print(Y[N//2-1])
