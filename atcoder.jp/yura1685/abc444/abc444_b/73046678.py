N, K = map(int,input().split())
ans = 0
for i in range(1,N+1):
    M = str(i)
    s = sum(int(m) for m in M)
    if s == K:
        ans += 1

print(ans)