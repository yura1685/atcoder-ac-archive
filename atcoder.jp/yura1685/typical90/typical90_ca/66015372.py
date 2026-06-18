H, W = map(int,input().split())
A = [list(map(int,input().split())) for _ in range(H)]
B = [list(map(int,input().split())) for _ in range(H)]

ans = 0
for h in range(H-1):
    for w in range(W-1):
        dis = B[h][w] - A[h][w]
        A[h][w] += dis
        A[h][w+1] += dis
        A[h+1][w] += dis
        A[h+1][w+1] += dis
        ans += abs(dis)

if A != B:
    print('No')
else:
    print('Yes'); print(ans)