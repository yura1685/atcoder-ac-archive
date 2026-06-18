S = [2**int(x) for x in input()]
X = [0] * (len(S)+1)
xor = 0
for i in range(len(S)):
    xor ^= S[i]
    X[i+1] = xor

from collections import Counter

C = Counter(X)

ans = 0
for c in C.values():
    ans += c*(c-1)//2

print(ans)