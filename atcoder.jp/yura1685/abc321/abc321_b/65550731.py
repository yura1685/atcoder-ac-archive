N, X = map(int,input().split())
A = sorted(list(map(int,input().split())))
score = sum(A[1:N-2])
if score + A[0] >= X:
    print(0)
elif score + A[-1] >= X:
    print(X-score)
else:
    print(-1)