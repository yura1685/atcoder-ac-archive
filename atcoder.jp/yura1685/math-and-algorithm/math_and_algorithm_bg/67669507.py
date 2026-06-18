N = int(input())
A = sorted(map(int,input().split()))

mod = 10**9 + 7
ans = 0
for i in range(N):
    ans += A[i]*pow(2,i,mod)
    ans %= mod
print(ans)