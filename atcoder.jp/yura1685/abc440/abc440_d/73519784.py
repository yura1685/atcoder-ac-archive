from bisect import bisect_left

I = input().split()
N, Q = int(I[0]), int(I[1])
A = sorted(map(int,input().split()))
for _ in range(Q):
    I = input().split()
    x, y = int(I[0]), int(I[1])
    pos = bisect_left(A, x)
    l, r = pos-1, N
    while r - l > 1:
        mid = (l + r) // 2
        if (A[mid] - x + 1) - (mid - pos + 1) >= y:
            r = mid
        else:
            l = mid
    print(x + (y-1) + (r - pos))
    