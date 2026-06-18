from math import sqrt

a, b, c = map(int,input().split())

if c - a - b < 0:
    print('No')
    exit()

m = 4*a*b
n = (c-a-b)**2
print('Yes' if m < n else 'No')