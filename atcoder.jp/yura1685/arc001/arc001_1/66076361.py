from collections import Counter

N = int(input())
c = input()
d = Counter(c)
D = list(d.values())
if len(D) <= 3:
  D.append(0)
print(max(D),min(D))