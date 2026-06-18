N = int(input())
S = [input() for _ in range(N)]
T = [input() for _ in range(N)]

if sum(x.count('#') for x in S) != sum(x.count('#') for x in T):
    exit(print('No'))

flag = False
for h in range(N):
    for w in range(N):
        if S[h][w] == "#":
            a, b = h, w
            flag = True
            break
    if flag:
        break

s = set()
for h in range(N):
    for w in range(N):
        if S[h][w] == "#":
            s.add((h-a,w-b))

def f(x,y,pat):
    if pat == 0:
        return (x, y)
    elif pat == 1:
        return (-x, -y)
    elif pat == 2:
        return (-y, x)
    else:
        return (y, -x)

for pat in range(4):
    for h in range(N):
        for w in range(N):
            if T[h][w] != '#':
                continue
            
            flag = True
            for dh, dw in s:
                nh, nw = f(dh, dw, pat)
                if 0 <= h + nh < N and 0 <= w + nw < N and T[h+nh][w+nw] == '#':
                    continue
                else:
                    flag = False
                    break
            if flag:
                exit(print('Yes'))
print('No')