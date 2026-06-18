N, M = map(int,input().split())
X = [int(x) for x in input().split()]
X.sort()
Y = [X[i+1] - X[i] for i in range(M-1)]
Y.sort(reverse=True)
print(X[M-1]-X[0]-sum(Y[:N-1]))