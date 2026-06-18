N, K = map(int,input().split())

X = []
for _ in range(N):
    s = int(input())
    if s == 0:
        exit(print(N))
    X.append(s)

r, ans, tmp = 0, 0, 1
for l in range(N):
    while r < N and tmp * X[r] <= K:
        tmp *= X[r]
        r += 1
    ans = max(ans,r-l)
    if l == r:
        r += 1
    else:
        tmp //= X[l]

print(ans)