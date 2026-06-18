N, M = map(int, input().split())
s = [input() for _ in range(N)]
ans = [[''] * M for _ in range(N)]
dir = [-1, 0, 1]
for h in range(N):
    for w in range(M):
        cnt = 0
        for dh in dir:
            for dw in dir:
                nh, nw = h + dh, w + dw
                if 0 <= nh < N and 0 <= nw < M and s[nh][nw] == '#':
                    cnt += 1
        ans[h][w] = str(cnt)

for L in ans:
    print(''.join(L))