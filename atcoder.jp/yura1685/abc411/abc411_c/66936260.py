N, Q = map(int,input().split())
A = list(map(int,input().split()))

col = [0]*(N+2)

ans = 0
for a in A:
    if col[a] == 0:
        col[a] = 1
        c = [col[a-1], col[a+1]]
        if c.count(1) == 2:
            ans -= 1
        elif c.count(1) == 1:
            pass
        else:
            ans += 1
    elif col[a] == 1:
        col[a] = 0
        c = [col[a-1], col[a+1]]
        if c.count(1) == 2:
            ans += 1
        elif c.count(1) == 1:
            pass
        else:
            ans -= 1
    print(ans)