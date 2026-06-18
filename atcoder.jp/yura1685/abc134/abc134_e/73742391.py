from sortedcontainers import SortedList

N = int(input())
S = SortedList()

for _ in range(N):
    A = int(input())
    idx = S.bisect_left(A)
    if idx == 0:
        S.add(A)
    else:
        n = S[idx-1]
        S.discard(n)
        S.add(A)

print(len(S))