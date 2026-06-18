S = list(map(str,input().split('|')))
c = []
for i in S:
    c.append(len(i))
c.pop(0)
c.pop(-1)
print(*c)