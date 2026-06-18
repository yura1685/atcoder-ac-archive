def solve():
    N, C = map(int,input().split())
    C -= 1
    dp = [list(input()) for _ in range(N)]
    A = [[] for _ in range(N)]
    for h in range(N):
        for w in range(N):
            if dp[h][w] == '#':
                A[w].append(h)
    dp[N-1][C] = 'o'
    m = [-1,0,1]
    for i in range(N-1,0,-1):
        for j in range(N):
            if dp[i][j] != 'o':
                continue
            for dj in m:
                if 0 <= j + dj < N:
                    if dp[i-1][j+dj] == '.':
                        dp[i-1][j+dj] = 'o'
                    elif dp[i-1][j+dj] == '#':
                        if A[j+dj] and A[j+dj][-1] == i-1:
                            A[j+dj].pop()
                            dp[i-1][j+dj] = 'o'
    ans = ['1' if x == 'o' else '0' for x in dp[0]]
    print(''.join(ans))
    dp.clear()
    A.clear()

T = int(input())
for _ in range(T):
    solve()