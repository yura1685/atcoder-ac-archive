from math import ceil
A, B = map(int,input().split())

n = A/B
l = int(n)
r = ceil(n)

if n-l < r-n:
    print(l)
else:
    print(r)