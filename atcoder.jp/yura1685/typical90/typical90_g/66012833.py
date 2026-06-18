import bisect

N = int(input())
A = list(map(int,input().split()))
A.sort()
A.append(10**20)

Q = int(input())
for _ in range(Q):
    B = int(input())
    l = bisect.bisect_left(A,B)
    r = bisect.bisect_right(A,B)
    if l != r:
        print(0)
    else:
        print(min(abs(A[l-1]-B), abs(A[l]-B)))