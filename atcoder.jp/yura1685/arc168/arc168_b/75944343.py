from collections import Counter

N = int(input())
A = Counter(map(int, input().split()))
B = []
for a, cnt in A.items():
    if cnt % 2 == 1:
        B.append(a)

xor = 0
for b in B: xor ^= b

if xor > 0: print(-1)
elif len(B) == 0: print(0)
else: print(max(B) - 1)