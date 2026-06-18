from atcoder.dsu import DSU

H, W = map(int,input().split())
S = [['=']+list(input())+['='] for _ in range(H)]
S = [['=']*(W+2)] + S + [['=']*(W+2)]
uf = DSU((H+2)*(W+2))

for h in range(H+2):
    for w in range(W+2):
        if S[h][w] != '#': continue
        if S[h-1][w] == '#': uf.merge(h*W+w,(h-1)*W+w)
        if S[h][w+1] == '#': uf.merge(h*W+w,h*W+w+1)

cnt = 1
leader = [0] * ((H+2)*(W+2))
for h in range(H+2):
    for w in range(W+2):
        if S[h][w] != '#': continue
        if leader[uf.leader(h*W+w)] == 0:
            leader[uf.leader(h*W+w)] = cnt
            cnt += 1
cnt -= 1
group = [[0]*(W+2) for _ in range(H+2)]
for h in range(H+2):
    for w in range(W+2):
        if S[h][w] != '#': continue
        group[h][w] = leader[uf.leader(h*W+w)]

ans = 0
c = [(-1,0),(0,-1),(0,1),(1,0)]
red = 0
for h in range(1,H+1):
    for w in range(1,W+1):
        if S[h][w] != '.': continue
        red += 1
        s = set()
        for dh, dw in c:
            if group[h+dh][w+dw] > 0: s.add(group[h+dh][w+dw])
        ans += cnt - len(s) + 1

mod = 998244353
print(ans * pow(red,mod-2,mod) % mod)