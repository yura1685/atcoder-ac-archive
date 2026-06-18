from collections import defaultdict

N, K = map(int,input().split())
A = list(map(int,input().split()))

l, r = 0, 0
cnt = 0
d = defaultdict(int)
ans = 0

while True:
    # 右端を伸ばすフェーズ
    while cnt <= K and r < N:
        new = A[r]
        if d[new] > 0:
            d[new] += 1
            r += 1
        else:
            if cnt < K:
                d[new] += 1
                r += 1
                cnt += 1
            else:
                break
    ans = max(ans,r-l)
    # 左端を縮めるフェーズ
    while l < r:
        old = A[l]
        d[old] -= 1
        l += 1
        if d[old] == 0:
            cnt -= 1
            break
    if r == N:
        break

print(ans)