N = int(input())

seg = []
for _ in range(N):
    t, x, y = map(int,input().split())
    if t == 1:
        seg.append((x,y))
    if t == 2:
        seg.append((x,y-0.1))
    if t == 3:
        seg.append((x+0.1,y))
    if t == 4:
        seg.append((x+0.1,y-0.1))

ans = 0
for i in range(N-1):
    for j in range(i+1,N):
        xi, yi = seg[i]
        xj, yj = seg[j]
        if xi <= xj <= yi or \
           xi <= yj <= yi or \
           xj <= xi <= yi <= yj or \
           xi <= xj <= yj <= yi:
            ans += 1

print(ans)