N, Q = map(int,input().split())

ring = [i for i in range(N+1)]
l, r = 1, 2

ans = 0
for _ in range(Q):
    H, T = map(str,input().split())
    T = int(T)
    if H == 'R':
        if r == T:
            continue
        if l < r:
            if l < T < r:
                ans += r-T
            elif r < T:
                ans += T-r
            else:
                ans += N+T-r
        else:
            if r < T < l:
                ans += T-r
            elif T < r:
                ans += r-T
            else:
                ans += N+r-T
        r = T
    if H == 'L':
        if l == T:
            continue
        if r < l:
            if r < T < l:
                ans += l-T
            elif l < T:
                ans += T-l
            else:
                ans += N+T-l
        else:
            if l < T < r:
                ans += T-l
            elif T < l:
                ans += l-T
            else:
                ans += N+l-T
        l = T
print(ans)