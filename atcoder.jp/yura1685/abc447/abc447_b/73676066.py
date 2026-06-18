from collections import Counter
S = list(input())
C = Counter(S)
M = max(C.values())

ans = [t for t in S if C[t] < M]
print(''.join(ans))