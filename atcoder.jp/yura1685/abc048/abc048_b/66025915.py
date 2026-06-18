from math import ceil

a, b, x = map(int,input().split())

l = ceil(a/x)
r = int(b/x)

for i in range(l-50,l+50):
    if i*x >= a:
        L = i
        break

for j in range(r-50,r+50):
    if j*x > b:
        R = j-1
        break

print(R-L+1)