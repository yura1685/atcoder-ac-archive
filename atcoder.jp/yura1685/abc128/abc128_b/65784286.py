n = int(input())
d = {}
for num in range(1,n+1):
    s, p = map(str,input().split())
    p = int(p)
    if d.get(s) == None:
        d[s] = [(p, num)]
    else:
        d[s].append((p, num))

c = sorted(d)
for city in c:
    restaurant = sorted(d[city], reverse=True)
    for info in restaurant:
        print(info[1])