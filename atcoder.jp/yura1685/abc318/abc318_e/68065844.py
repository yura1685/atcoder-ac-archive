from collections import defaultdict

d = defaultdict(list)
N = int(input())
A = list(map(int,input().split()))
for i in range(N):
    d[A[i]].append(i)

ans = 0
for v in d.values():
    ansv = 0
    n = len(v)
    for i in range(n):
        ansv += (2*i+1-n)*v[i]
    ans += ansv - (n-1)*n*(n+1)//6

print(ans)