N = int(input())
W = list(map(int,input().split()))
ans = 10000
for i in range(N+1):
    ans = min(ans, abs(sum(W[:i]) - sum(W[i:])))
print(ans)