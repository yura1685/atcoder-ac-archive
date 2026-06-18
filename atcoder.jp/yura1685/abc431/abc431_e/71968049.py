from collections import deque

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
d = {"A": 0, "B": 1, "C": 3}


def solve():
    h, w = map(int, input().split())
    s = [input() for i in range(h)]
    dp = [[[1 << 30] * 4 for _ in range(w)] for _ in range(h)]

    dq = deque()
    dq.append((0, 0, -1, 1))
    while dq:
        c, pre_x, pre_y, dir = dq.popleft()
        x, y = pre_x + dx[dir], pre_y + dy[dir]
        if not (0 <= x < h and 0 <= y < w):
            continue
        for ndir in range(4):
            if dir ^ ndir == 2:
                continue
            if dir ^ ndir == d[s[x][y]]:
                # cost : 0
                if c < dp[x][y][ndir]:
                    dp[x][y][ndir] = c
                    dq.appendleft((c, x, y, ndir))
            else:
                # cost : 1
                if c + 1 < dp[x][y][ndir]:
                    dp[x][y][ndir] = c + 1
                    dq.append((c + 1, x, y, ndir))

    print(dp[h - 1][w - 1][1])


for _ in range(int(input())):
    solve()
