a, b, c, d, e, f = map(int,input().split())
a = a % 998244353
b = b % 998244353
c = c % 998244353
d = d % 998244353
e = e % 998244353
f = f % 998244353

print((a*b*c-d*e*f)%998244353)