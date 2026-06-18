from collections import Counter

N, K = map(int, input().split())
A = list(map(int, input().split()))
C = Counter(A)

L = [a*c for a, c in C.items()]
L.sort()
for _ in range(K):
    if L:
        L.pop()
    else:
        break

print(sum(L))