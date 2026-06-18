from atcoder.maxflow import MFGraph

N, M = map(int,input().split())
s = N * M
t = N * M + 1
S = [list(input()) for _ in range(N)]

g = MFGraph(t + 1)

def enc(i, j): # グリッド(i,j)を数字に
    return i * M + j

def dec(v): # 数字からグリッドに
    return v//M, v % M

for i in range(N):
    for j in range(M):
        if S[i][j] == '#':
            continue
        if (i+j) % 2 == 0:
            g.add_edge(s, enc(i,j), 1)
        else:
            g.add_edge(enc(i,j), t, 1)

dx = [1,0,-1,0]
dy = [0,1,0,-1]
for i in range(N):
    for j in range(M):
        if (i+j) % 2 == 1 or S[i][j] == '#':
            continue
        for d in range(4):
            ii = i + dx[d]
            jj = j + dy[d]
            if 0 <= ii < N and 0 <= jj < M and S[ii][jj] == '.':
                g.add_edge(enc(i,j), enc(ii,jj), 1)

print(g.flow(s, t))

for e in g.edges():
    if e.src == s or e.dst == t or e.flow == 0:
        continue
    (i,j) = dec(e.src)
    (ii,jj) = dec(e.dst)
    if i == ii + 1:
        S[ii][jj] = 'v'
        S[i][j] = '^'
    elif i == ii - 1:
        S[i][j] = 'v'
        S[ii][jj] = '^'
    elif j == jj + 1:
        S[ii][jj] = '>'
        S[i][j] = '<'
    else:
        S[i][j] = '>'
        S[ii][jj] = '<'

for r in S:
    print(''.join(r))