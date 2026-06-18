inf = 10 ** 18
N = int(input())
P = []
M, Mxy = 0, 0
for _ in range(N):
    X, Y, U = input().split()
    X, Y = int(X), int(Y)
    M = max(M, X + Y)
    Mxy = max(Mxy, X, Y)
    P.append([X, Y, U])

UD = [[] for _ in range(Mxy + 1)]
RL = [[] for _ in range(Mxy + 1)]
for x, y, u in P:
    if u == 'U':
        UD[x].append(y+1)
    elif u == 'D':
        UD[x].append(-y-1)
    elif u == 'R':
        RL[y].append(x+1)
    elif u == 'L':
        RL[y].append(-x-1)

def line(L):
    res = inf
    for LL in L:
        if len(LL) < 2: continue
        LL.sort(key=lambda x:abs(x))
        m, p = inf, -inf
        for x in LL:
            if x > 0:
                p = x
            else:
                m = -x
                res = min(res, 5 * (m - p))
    return res

def perp(L):
    res = inf
    lines = {}
    for x, y, u in L:
        if u in 'UR':
            lines.setdefault(x + y, []).append((x, u))
    for v in lines.values():
        if len(v) < 2: continue
        v.sort()
        for i in range(len(v) - 1):
            if v[i][1] == 'R' and v[i+1][1] == 'U':
                res = min(res, v[i+1][0] - v[i][0])
    return 10 * res

ans = min(inf, line(UD), line(RL))
dir = {'U':'L', 'L':'D', 'D':'R', 'R':'U'}

for i in range(4):
    ans = min(ans, perp(P))
    if i == 3: break
    for j in range(N):
        x, y, u = P[j]
        P[j] = [Mxy - y, x, dir[u]]

print(ans if ans < inf else 'SAFE')