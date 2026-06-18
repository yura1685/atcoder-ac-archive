from sortedcontainers import SortedList

N, M = map(int,input().split())
A = list(map(int,input().split()))

counter = [0] * N
sl = SortedList(i for i in range(N+1))

for i in range(M):
    sl.discard(A[i])
    counter[A[i]] += 1

ans = sl[0]
for i in range(N-M):
    l, r = i, i+M
    counter[A[l]] -= 1
    if counter[A[l]] == 0:
        sl.add(A[l])
    if counter[A[r]] == 0:
        sl.discard(A[r])
    counter[A[r]] += 1
    ans = min(ans,sl[0])

print(ans)