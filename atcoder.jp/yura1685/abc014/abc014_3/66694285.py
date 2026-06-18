from itertools import accumulate

n = int(input())
l = [0]*(1000002)
for _ in range(n):
    a, b = map(int,input().split())
    l[a] += 1
    l[b+1] -= 1

c = list(accumulate(l))

m = 0
for i in c:
    m = max(m, i)
print(m)