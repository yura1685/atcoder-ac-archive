from bisect import bisect_left, bisect_right

line1 = input().split()
N, Q = int(line1[0]), int(line1[1])
S = sorted(map(int,input().split()))

for _ in range(Q):
    line = input().split()
    b, k = int(line[0]), int(line[1])
    l, r = 0, 10**9
    while r - l > 1:
        mid = (l+r)//2
        bl = bisect_left(S, b-mid)
        br = bisect_right(S, b+mid)
        if br - bl < k:
            l = mid
        else:
            r = mid

    if bisect_right(S,b+l) - bisect_left(S,b-l) >= k:
        print(l)
    else:
        print(r)