H, W, N = map(int,input().split())
A = [list(map(int,input().split())) for _ in range(H)]
cnt = [0]*H
for _ in range(N):
    B = int(input())
    for h in range(H):
        for w in range(W):
            if A[h][w] == B:
                cnt[h] += 1

print(max(cnt))