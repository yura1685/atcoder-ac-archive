N = int(input())
z = [tuple(map(int,input().split())) for _ in range(N)]
S = input()
d = {}

for i in range(N):
    x, y = z[i]
    v = S[i]
    if d.get(y) == None:
        if v == 'R':
            c = [x, -10**10]
        else:
            c = [10**10, x]
        d[y] = c
    else:
        if v == 'L':
            d[y][1] = max(d[y][1], x)
        else:
            d[y][0] = min(d[y][0], x)

for key in d:
    if d[key][1] - d[key][0] > 0:
        print('Yes')
        exit()
print('No')