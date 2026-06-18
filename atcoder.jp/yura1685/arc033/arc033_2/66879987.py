from collections import defaultdict

Na, Nb = map(int,input().split())
A = set(list(map(int,input().split())))
B = set(list(map(int,input().split())))

d = defaultdict(int)

for a in A:
    d[a] += 1
for b in B:
    d[b] += 1

A |= B
print(list(d.values()).count(2)/len(A))