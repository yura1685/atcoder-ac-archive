from sortedcontainers import SortedList

N, Q = map(int,input().split())
S = SortedList(map(int,input().split()))

for _ in range(Q):
    b, k = map(int,input().split())
    l, r = 0, 10**9
    while r - l > 1:
        mid = (l+r)//2
        bl = S.bisect_left(b-mid)
        br = S.bisect_right(b+mid)
        if br - bl < k:
            l = mid
        else:
            r = mid
            
    if S.bisect_right(b+l) - S.bisect_left(b-l) >= k:
        print(l)
    else:
        print(r)