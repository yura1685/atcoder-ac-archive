from collections import Counter

S = input()
c = Counter(S)

odd, even = 0, 0
for i in c.values():
    odd += i % 2
    even += i//2

if odd == 0:
    print(2*even)
else:
    print(even//odd*2 + 1)