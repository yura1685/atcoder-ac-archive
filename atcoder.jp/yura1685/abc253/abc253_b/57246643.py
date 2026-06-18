H, W = map(int,input().split())
glid = ['']*H
for i in range(H):
    glid[i] = list(input())
point_count = 0
for i in range(H):
    if 'o' in glid[i]:
        for j in range(W):
            if glid[i][j] == 'o' and point_count == 0:
                x1, y1 = i, j
                point_count += 1
            elif glid[i][j] == 'o' and point_count == 1:
                x2, y2 = i, j
                point_count += 1
            if point_count == 2:
                break
        if point_count == 2:
            break
print(abs(x1-x2)+abs(y1-y2))