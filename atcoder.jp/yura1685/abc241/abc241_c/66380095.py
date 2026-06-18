def solve(g):
    for v in g:
        if v.count('#') >= 4:
            return True
    z = list(zip(*g))
    for v in z:
        if v.count('#') >= 4:
            return True
    a, b = 0, 0
    for i in range(6):
        if g[i][i] == '#':
            a += 1
        if g[5-i][i] == '#':
            b += 1
    if a >= 4 or b >= 4:
        return True
    return False

N = int(input())

glid = [input() for _ in range(N)]

for h in range(N-5):
    for w in range(N-5):
        hoge = [glid[w+i][h:h+6] for i in range(6)]
        if solve(hoge):
            print('Yes')
            exit()
print('No')