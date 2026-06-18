H, W = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(H)]

ans = []
for h in range(H):
    for w in range(W-1):
        if A[h][w] % 2 == 1:
            A[h][w] -= 1
            A[h][w+1] += 1
            ans.append((h+1, w+1, h+1, w+2))
for h in range(H-1):
    if A[h][-1] % 2 == 1:
        A[h][-1] -= 1
        A[h+1][-1] += 1
        ans.append((h+1, W, h+2, W))

print(len(ans))
for t in ans: print(*t)