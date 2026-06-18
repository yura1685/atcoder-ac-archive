from bisect import *

N = int(input())
L = list(map(int,input().split()))
L.sort()

ans = 0
for i in range(N-2):
    for j in range(i+1,N-1):
        a = L[i]
        b = L[j]
        ans += bisect(L,a+b-1) - j - 1

print(ans)