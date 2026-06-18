H, W, Y, X = map(int,input().split())
glid = [input() for _ in range(H)]
T = input()
house = []
for i in range(len(T)):
    move = T[i]
    if move == 'L':
        if X != 1:
            if glid[Y-1][X-2] != "#":
                X -= 1
        if glid[Y-1][X-1] == '@':
            house.append((X,Y))
    if move == 'R':
        if X != W:
            if glid[Y-1][X] != "#":
                X += 1
        if glid[Y-1][X-1] == '@':
            house.append((X,Y))
    if move == 'U':
        if Y != 1:
            if glid[Y-2][X-1] != "#":
                Y -= 1
        if glid[Y-1][X-1] == '@':
            house.append((X,Y))
    if move == 'D':
        if Y != H:
            if glid[Y][X-1] != "#":
                Y += 1
        if glid[Y-1][X-1] == '@':
            house.append((X,Y))
print(Y,X,len(set(house)))