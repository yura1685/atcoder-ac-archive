import bisect

N, M, D = map(int,input().split())
A = list(map(int,input().split()))
B = list(map(int,input().split()))
if N > M:
    A, B = B, A
A.sort(); B.sort()

ans = -1

for a in A:
    right = bisect.bisect(B, a+D)
    left  = bisect.bisect_left(B, a-D)
    if right != left:
        c = B[right-1]
        ans = max(ans, a+c)

print(ans)