H, W, X, Y = map(int,input().split())
glid = ['']*H

for i in range(H):
    glid[i] = input()

vision = 0

point = 0
while glid[X-1][Y-1+point] != '#':
    vision += 1
    point += 1
    if Y-1+point == W:
        break
vision -= 1

point = 0
while glid[X-1][Y-1-point] != '#':
    vision += 1
    point += 1
    if Y-1-point == -1:
        break
vision -= 1

point = 0
while glid[X-1+point][Y-1] != '#':
    vision += 1
    point += 1
    if X-1+point == H:
        break
vision -= 1

point = 0
while glid[X-1-point][Y-1] != '#':
    vision += 1
    point += 1
    if X-1-point == -1:
        break
vision -= 1

vision += 1
print(vision)