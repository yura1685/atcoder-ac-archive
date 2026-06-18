N, M, Q = map(int,input().split())
A = []
for _ in range(N):
    W, V = map(int,input().split())
    A.append((V,W))
A.sort(reverse=True)
X = list(map(int,input().split()))
for _ in range(Q):
    ans = 0
    L, R = map(int,input().split())
    box = X[:L-1] + X[R:]
    for v, w in A:
        if not box:
            break
        p = 16851685
        for x in box:
            if x >= w:
                p = min(p,x)
        if p == 16851685:
            continue
        else:
            ans += v
            box.remove(p)
    print(ans)