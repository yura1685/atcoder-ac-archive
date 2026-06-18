import bisect

N, M = map(int,input().split())
A = sorted(list(map(int,input().split())))
present = 0
for i in range(N):
    left = A[i]
    right_max = left + M
    get = bisect.bisect_left(A,right_max)
    present = max(present, get-i)
print(present)