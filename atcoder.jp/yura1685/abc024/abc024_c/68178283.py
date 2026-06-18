N, D, K = map(int,input().split())

move = [tuple(map(int,input().split())) for _ in range(D)]

for _ in range(K):
    now, goal = map(int,input().split())
    ans = 0
    for l, r in move:
        ans += 1
        if not l <= now <= r:
            continue
        if l <= goal <= r:
            print(ans)
            break
        if goal < l:
            now = l
        if r < goal:
            now = r
    