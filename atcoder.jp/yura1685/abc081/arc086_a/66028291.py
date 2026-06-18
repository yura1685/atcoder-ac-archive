from collections import Counter

n, k = map(int,input().split())
a = list(map(int,input().split()))

c = Counter(a)
x = list(c.values())
x.sort()

N = len(x)
if N <= k:
    print(0)
    exit()

print(sum(x[:-k]))