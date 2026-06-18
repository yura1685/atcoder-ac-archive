N, M = map(int,input().split())
S = input()
T = input()

ans = 100000
for i in range(N-M+1):
    X = S[i:i+M]
    cnt = 0
    for j in range(M):
        x, y = X[j], T[j]
        cnt += (int(x) - int(y)) % 10
    ans = min(ans, cnt)

print(ans)