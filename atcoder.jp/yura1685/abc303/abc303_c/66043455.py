N, M, H, K = map(int, input().split())
S = input()

items = set()
for _ in range(M):
    x, y = map(int, input().split())
    items.add((x, y))

x, y = 0, 0
for move in S:
    H -= 1
    if H < 0:
        print("No")
        exit()
    
    if move == 'R':
        x += 1
    elif move == 'L':
        x -= 1
    elif move == 'U':
        y += 1
    elif move == 'D':
        y -= 1

    if (x, y) in items and H < K:
        items.remove((x, y))
        H = K

print("Yes")
