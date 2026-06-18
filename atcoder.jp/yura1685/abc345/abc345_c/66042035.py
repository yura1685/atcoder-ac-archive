from collections import Counter

S = input()
n = len(S)
d = Counter(S)
c = list(d.values())


noch = 0
for i in c:
    noch += i*(i-1)//2

ans = n*(n-1)//2 - noch
if noch > 0:
    ans += 1

print(ans)