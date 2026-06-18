from collections import Counter

N = int(input())
D = list(map(int,input().split()))
mod = 998244353

if D[0] != 0 or D.count(0) > 1:
    print(0); exit()

M = max(D)
d = Counter(D)

ans = 1
for i in range(1,M+1):
    ans *= pow(d[i-1],d[i],mod)
    ans %= mod

print(ans)