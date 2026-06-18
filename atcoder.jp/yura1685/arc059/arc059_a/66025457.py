from math import ceil
n = int(input())
a = list(map(int,input().split()))
d = sum(a)/n
x1 = int(d)
x2 = ceil(d)

ans1, ans2 = 0, 0

for i in range(n):
    ans1 += (a[i]-x1)**2
    ans2 += (a[i]-x2)**2

print(min(ans1,ans2))