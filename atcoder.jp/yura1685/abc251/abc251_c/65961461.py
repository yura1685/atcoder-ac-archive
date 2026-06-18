n = int(input())
d = {}
d2 = {}
original = []
for i in range(1,n+1):
    s, p = map(str,input().split())
    p = int(p)
    if d.get(s) == None:
        d[s] = 1
        if d2.get(p) == None:
            d2[p] = [i]
        else:
            d2[p].append(i)
print(min(d2[max(d2)]))