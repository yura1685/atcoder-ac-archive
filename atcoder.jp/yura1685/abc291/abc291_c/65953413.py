N = int(input())
S = input()

d = set([(0,0)])
n = 1

x, y = 0, 0
for i in range(N):
    s = S[i]
    if s == 'R':
        x += 1
    elif s == 'L':
        x -= 1
    elif s == 'U':
        y += 1
    else:
        y -= 1
    d.add((x,y))
    if len(d) <= n:
        print('Yes')
        exit()
    n += 1
print('No')