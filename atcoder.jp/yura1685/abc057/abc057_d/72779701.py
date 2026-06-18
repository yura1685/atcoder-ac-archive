from math import comb

n, a, b = map(int,input().split())
v = sorted(map(int,input().split()), reverse=True)

sup = 0
for i in range(a,b+1):
    sup = max(sup, sum(v[:i])/i)

ans = 0
for i in range(a,b+1):
    if sum(v[:i])/i != sup:
        continue
    x, y = v[:i].count(v[i-1]), v[i:].count(v[i-1])
    ans += comb(x+y,x)

# 誤差が怖い
print(sup)
print(ans)