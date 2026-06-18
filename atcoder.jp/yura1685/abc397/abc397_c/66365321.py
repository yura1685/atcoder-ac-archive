from collections import Counter

N = int(input())
A = list(map(int,input().split()))
c = Counter(A)
n = len(c)

l = {}
lenl = 0
ans = n

for i in range(N):
    a = A[i]
    if l.get(a) == None:
        l[a] = 1
        lenl += 1
    else:
        l[a] += 1
    if c[a] == l[a]:
        n -= 1
    ans = max(ans, n+lenl)

print(ans)