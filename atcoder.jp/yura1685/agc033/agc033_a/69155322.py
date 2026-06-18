from collections import deque

H, W = map(int,input().split())
A = [list(input()) for _ in range(H)]
d = deque()
for h in range(H):
    for w in range(W):
        if A[h][w] == '#':
            d.append((h,w))

ans = 0
while d:
    ans += 1
    N = len(d)
    for _ in range(N):
        h, w = d.popleft()
        if h != 0 and A[h-1][w] == '.':
            A[h-1][w] = '#'
            d.append((h-1,w))
        if w != 0 and A[h][w-1] == '.':
            A[h][w-1] = '#'
            d.append((h,w-1))
        if h != H-1 and A[h+1][w] == '.':
            A[h+1][w] = '#'
            d.append((h+1,w))
        if w != W-1 and A[h][w+1] == '.':
            A[h][w+1] = '#'
            d.append((h,w+1))

print(ans-1)