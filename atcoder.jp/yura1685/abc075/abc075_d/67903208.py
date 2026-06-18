N, K = map(int,input().split())
P, X, Y = [], [], []
for _ in range(N):
    x, y = map(int,input().split())
    P.append((x,y))
    X.append(x)
    Y.append(y)

X.sort()
Y.sort()

ans = float('inf')
for l in range(N-1):
    for r in range(l+1,N):
        for d in range(N-1):
            for u in range(d+1,N):
                L, R, D, U = X[l], X[r], Y[d], Y[u]
                cnt = 0
                for x, y in P:
                    if L <= x <= R and D <= y <= U:
                        cnt += 1
                if cnt >= K:
                    ans = min(ans,(R-L)*(U-D))

print(ans)