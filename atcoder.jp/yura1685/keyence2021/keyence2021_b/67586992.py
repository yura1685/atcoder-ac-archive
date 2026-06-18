from bisect import *

N, K = map(int,input().split())
A = list(map(int,input().split()))
A.sort()

num = [0]*N
for i in range(max(A)+1):
    num[i] = min(bisect(A,i) - bisect_left(A,i), K)

ans = 0
left = K
for i in range(N):
    if num[i] < left:
        ans += i * (left - num[i])
        left = num[i]
    if left == 0:
        break

print(ans)