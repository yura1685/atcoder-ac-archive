from collections import Counter

N = int(input())
A = list(map(int,input().split()))
C = Counter(A)
mod = 10 ** 9 + 7

if A[0] > 0 or C[0] > 1:
    exit(print(0))

ans = 1
for i in range(1,max(A)+1):
    X, Y = pow(2,C[i]*(C[i]-1)//2,mod), pow(pow(2,C[i-1],mod)-1,C[i],mod)
    ans *= X * Y
    ans %= mod

print(ans)