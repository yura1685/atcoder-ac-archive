from collections import defaultdict

N = int(input())
A = [list(map(int,input().split())) for _ in range(N)]

P = [[defaultdict(int) for _ in range(N)] for _ in range(N)]
P[0][0][A[0][0]] = 1
for h in range(N):
    for w in range(N):
        if h + w >= N-1:
            continue
        for val, cnt in P[h][w].items():
            if h + 1 < N:
                P[h+1][w][val^A[h+1][w]] += cnt
            if w + 1 < N:
                P[h][w+1][val^A[h][w+1]] += cnt

Q = [[defaultdict(int) for _ in range(N)] for _ in range(N)]
Q[N-1][N-1][A[N-1][N-1]] = 1
for h in range(N-1,-1,-1):
    for w in range(N-1,-1,-1):
        if h + w <= N-1:
            continue
        for val, cnt in Q[h][w].items():
            if h - 1 >= 0:
                Q[h-1][w][val^A[h-1][w]] += cnt
            if w - 1 >= 0:
                Q[h][w-1][val^A[h][w-1]] += cnt

ans = 0
for h in range(N):
    w = N - 1 - h
    for val, cnt in P[h][w].items():
        valQ = val ^ A[h][w]
        if valQ in Q[h][w]:
            ans += cnt * Q[h][w][valQ]

print(ans)