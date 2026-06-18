from collections import deque, defaultdict

H, W = map(int,input().split())
glid = ['#'*(W+2)]+['#'+input()+'#' for _ in range(H)]+['#'*(W+2)]
H, W = H+2, W+2
dd = defaultdict(list)
for h in range(H):
    for w in range(W):
        if glid[h][w] in '.#':
            continue
        dd[glid[h][w]].append((h,w))
sh, sw = dd['S'][0]

dq = deque()
dq.append((sh,sw))
INF = float('INF')
time = [[INF]*W for _ in range(H)]
time[sh][sw] = 0
c = [(-1,0),(0,-1),(0,1),(1,0)]
ans = INF
while dq:
    h, w = dq.popleft()
    # テレポートしない場合
    for dh, dw in c:
        h2, w2 = h+dh, w+dw
        if glid[h2][w2] == '#':
            continue
        if time[h2][w2] > time[h][w] + 1:
            time[h2][w2] = time[h][w] + 1
            dq.append((h2,w2))
    # その他の場合
    if glid[h][w] == 'G':
        ans = min(ans,time[h][w])
    if glid[h][w] in '.S':
        continue
    for h2, w2 in dd[glid[h][w]]:
        if (h,w) == (h2,w2):
            continue
        if time[h2][w2] > time[h][w] + 1:
            time[h2][w2] = time[h][w] + 1
            dq.append((h2,w2))
    del dd[glid[h][w]]

print(ans if ans < INF else -1)