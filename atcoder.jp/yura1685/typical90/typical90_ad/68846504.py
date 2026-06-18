N, K = map(int,input().split())
P = [0] * (N+1)

for p in range(2,N+1):
    if P[p] > 0:
        continue
    for i in range(p,N+1,p):
        P[i] += 1

ans = 0
for n in P:
    if n >= K:
        ans += 1

print(ans)