from collections import Counter

N = int(input())
L = []
for i in range(N):
    L.append(input())
u, w = [], []
d = Counter(L)
for i in d:
    u.append(i)
    w.append(d[i])
k = w.index(max(w))
print(u[k])