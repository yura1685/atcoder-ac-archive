from collections import Counter

N = int(input())
c = []
for i in range(N):
    a = int(input())
    c.append(a)
d = set(c)
e = Counter(c)

ans = 0
for i in d:
    if e[i] % 2 == 1:
        ans += 1

print(ans)