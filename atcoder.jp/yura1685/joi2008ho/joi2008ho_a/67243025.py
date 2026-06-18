N = int(input())

stone = [0]
c = int(input())
stone = [(c,1)]

for i in range(N-1):
    c = int(input())
    if i % 2 == 1:
        color, num = stone.pop()
        if color == c:
            stone.append((color,num+1))
        else:
            stone.append((color,num))
            stone.append((c,1))
    else:
        color, num = stone.pop()
        if color == c:
            stone.append((color,num+1))
        else:
            color = c
            num += 1
            if stone:
                color2, num2 = stone.pop()
                num += num2
            stone.append((color,num))

ans = 0
for col, num in stone:
    if col == 0:
        ans += num
print(ans)