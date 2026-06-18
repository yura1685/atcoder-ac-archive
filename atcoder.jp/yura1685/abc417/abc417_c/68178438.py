from bisect import *

N = int(input())
A = list(map(int,input().split()))
B = [i+1+A[i] for i in range(N)]
B.sort()

ans = 0
for j in range(N):
    ans += bisect(B,j+1-A[j]) - bisect_left(B,j+1-A[j])

print(ans)