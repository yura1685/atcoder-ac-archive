N = int(input())
P = list(map(int,input().split()))

ans = 0
m = P[0]
for p in P:
    if p <= m:
        ans += 1
        m = p
print(ans)
