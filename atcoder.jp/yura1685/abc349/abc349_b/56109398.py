S = input()

d = {}

for i in S:
    d[i] = d.get(i,0) + 1

v = list(d.values())
for k in range(1,len(S)+1):
    if v.count(k) != 0 and v.count(k) != 2:
        print('No')
        exit()
        
print('Yes')