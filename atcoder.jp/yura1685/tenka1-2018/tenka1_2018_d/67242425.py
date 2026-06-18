from math import isqrt

N = int(input())
k = 0
for i in range(N+10):
    if i*(i-1) == 2*N:
        k = i
        break
if k == 0:
    print('No')
else:
    print('Yes')
    print(k)

ans = [set() for _ in range(k)]
cnt = 1
for i in range(k-1):
    for j in range(i+1,k):
        ans[i].add(cnt)
        ans[j].add(cnt)
        cnt += 1
for i in ans:
    print(k-1,*i)