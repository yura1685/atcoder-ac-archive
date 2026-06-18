def solve():
    N, M, K = map(int,input().split())
    S = input()
    g = [[] for _ in range(N)]
    for _ in range(M):
        U, V = map(int,input().split())
        g[V-1].append(U-1)
    dp = [[-1]*N for _ in range(2*K+1)] # 1→Alice win!
    for i in range(N):
        if S[i] == 'A': dp[0][i] = 1
        else: dp[0][i] = 0
    for turn in range(2*K):
        if turn % 2 == 0: # Bob's turn.
            for u in range(N):
                for v in g[u]:
                    if dp[turn][u] == 0:
                        dp[turn+1][v] = 0
            for u in range(N):
                if dp[turn+1][u] == -1:
                    dp[turn+1][u] = 1
        else:
            for u in range(N):
                for v in g[u]:
                    if dp[turn][u] == 1:
                        dp[turn+1][v] = 1
            for u in range(N):
                if dp[turn+1][u] == -1:
                    dp[turn+1][u] = 0
    print('Alice' if dp[-1][0] else 'Bob')

T = int(input())
for _ in range(T):
    solve()