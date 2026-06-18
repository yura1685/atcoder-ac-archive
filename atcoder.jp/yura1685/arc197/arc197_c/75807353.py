from atcoder.fenwicktree import FenwickTree

Q = int(input())
N = 2750160
L = [0] * N
FT = FenwickTree(N)
FT.add(0, 1)

for _ in range(Q):
    a, b = map(int, input().split())
    if a < N and L[a] == 0:
        for n in range(a, N, a):
            if L[n] == 0:
                L[n] = 1
                FT.add(n, 1)
    
    l, r = 0, N
    while r - l > 1:
        mid = (l + r) // 2
        cnt = mid - FT.sum(0, mid + 1) + 1
        if cnt < b:
            l = mid
        else:
            r = mid
    print(r)