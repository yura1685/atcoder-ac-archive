from collections import Counter

N = int(input())
name = []
Cl = []
for _ in range(N):
    s, t = input().split()
    name.append((s,t))
    Cl.append(s)
    Cl.append(t)
C = Counter(Cl)

for i in range(N):
    s, t = name[i]
    if s != t and C[s] > 1 and C[t] > 1:
        exit(print('No'))

print('Yes')