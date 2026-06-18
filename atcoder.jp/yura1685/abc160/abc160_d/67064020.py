N, X, Y = map(int,input().split())
X, Y = X-1, Y-1
ans = [0]*(N+1)

for i in range(N-1):
    for j in range(i+1,N):
        dis = min(j-i, abs(X-i)+1+abs(Y-j))
        ans[dis] += 1

for i in range(1,N):
    print(ans[i])