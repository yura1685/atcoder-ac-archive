N, K = map(int,input().split())
a = list(map(int,input().split()))

S = sum(a[:K])
ans = S
for i in range(N-K):
    S += a[i+K] - a[i]
    ans += S

print(ans)