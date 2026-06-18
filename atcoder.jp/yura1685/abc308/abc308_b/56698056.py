n, m = map(int,input().split())
c = list(map(str,input().split()))
d = list(map(str,input().split()))
p = list(map(int,input().split()))

u = {}
for i in range(m):
    u[d[i]] = p[i+1]

money = 0
for i in c:
    if i in u:
        money += u[i]
    else:
        money += p[0]
print(money)