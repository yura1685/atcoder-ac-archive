N = int(input())
A = list(map(int,input().split()))

ans = 0
for l in range(N):
    for r in range(l,N):
        X = A[l:r+1]
        S = sum(X)
        for x in X:
            if S % x == 0:
                break
        else:
            ans += 1

print(ans)