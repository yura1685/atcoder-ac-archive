from collections import defaultdict

N, M = map(int, input().split())
B = defaultdict(set)
for _ in range(M):
    X, Y = map(int, input().split())
    B[X].add(Y)

Sx = sorted(B.keys())
S = set([N])
for x in Sx:
    New = []
    Del = []
    for y in B[x]:
        if y - 1 in S or y + 1 in S:
            New.append(y)
        elif y in S:
            Del.append(y)
    for y in New:
        S.add(y)
    for y in Del:
        S.discard(y)

print(len(S))