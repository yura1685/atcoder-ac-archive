N = int(input())

py = [tuple(map(int,input().split())) for _ in range(N)]

for i in range(N):
    if py[i][2] != 0:
        ind = i
        break

for cx in range(101):
    for cy in range(101):
        x, y, h = py[ind]
        H = h + abs(x-cx) + abs(y-cy)
        for x, y, h in py:
            if max(H - abs(x-cx) - abs(y-cy),0) != h:
                break
        else:
            print(cx,cy,H)
            exit()