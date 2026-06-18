N = int(input())
A = list(map(int,input().split()))
A.sort()
mod = 998244353

ans = 0
rui = 0
for i in range(1,N):
    rui = 2*rui + A[i-1]
    rui %= mod
    ans += rui*A[i]
    ans %= mod

s2 = 0
for i in range(N):
    s2 += A[i]*A[i]
    s2 %= mod

print((ans+s2)%mod)