from sortedcontainers import SortedList

N, M = map(int, input().split())

A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = list(map(int, input().split()))
D = list(map(int, input().split()))

Q = []
for a, b in zip(A, B):
    Q.append((a, b, 1))
for c, d in zip(C, D):
    Q.append((c, d, 2))
Q.sort()

S = SortedList()
for x, y, t in Q:
    if t == 1:
        S.add(y)
    else:
        if not S or S[0] > y:
            pass
        else:
            idx = S.bisect_right(y)
            S.discard(S[idx-1])

print('No' if S else 'Yes')