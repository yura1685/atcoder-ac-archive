from collections import Counter

s = input()
d = Counter(s)
a = 0
for i in d:
    a = max(a,d[i])
print(sorted([k for k, v in d.items() if v == a])[0])