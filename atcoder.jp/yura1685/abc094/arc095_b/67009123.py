import bisect

N = int(input())
A = list(map(int,input().split()))
A.sort()
n = A[-1]
a, b = bisect.bisect(A,n//2), bisect.bisect_left(A,n//2)

if a != b:
    print(n,A[b])
else:
    x, y = A[a-1], A[a]
    if x < n-y:
        print(n,y)
    else:
        print(n,x)