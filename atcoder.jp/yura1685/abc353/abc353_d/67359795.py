from itertools import accumulate

N = int(input())
A = list(map(int,input().split()))
C = list(accumulate(A))

ans = 0
mod = 998244353

for i in range(1,N):
    x = (C[i-1]*10**len(str(A[i]))+A[i]*i)
    ans += x % mod

print(ans % mod)