from math import ceil

a, b, c, d = map(int,input().split())
if c*d - b <= 0:
    print(-1)
else:
    print(ceil(a/(c*d-b)))