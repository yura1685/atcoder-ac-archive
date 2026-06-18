from atcoder.dsu import DSU

H, W = map(int,input().split())
glid = [['#']*(W+2)] + [['#']+['.']*W+['#'] for _ in range(H)] + [['#']*(W+2)]

graph = DSU((H+2)*(W+2))
X = [(-1,0),(0,-1),(0,1),(1,0)]
def num(a,b):
    return a*(W+2)+b

Q = int(input())
for _ in range(Q):
    q = list(map(int,input().split()))
    if q[0] == 1:
        r, c = q[1:]
        glid[r][c] = 'R'
        for x, y in X:
            if glid[r+x][c+y] == 'R':
                graph.merge(num(r,c),num(r+x,c+y))
    else:
        ra, ca, rb, cb = q[1:]
        if glid[ra][ca] == glid[rb][cb] == 'R' and graph.same(num(ra,ca),num(rb,cb)):
            print('Yes')
        else:
            print('No')
    