H, W = map(int, input().split())
S = [input() for _ in range(H)]

def dfs(h, w, sh, sw):
    for dh, dw in [(-1, 0), (0, -1), (0, 1), (1, 0)]:
        nh, nw = h + dh, w + dw
        if not (0 <= nh < H and 0 <= nw < W):
            continue
        if S[nh][nw] == '#':
            continue
        if (nh, nw) == (sh, sw):
            global ans, length
            ans = max(ans, length)
        elif In[nh][nw] == True:
            pass
        else:
            In[nh][nw] = True
            length += 1
            dfs(nh, nw, sh, sw)
            In[nh][nw] = False
            length -= 1
    
ans = 0
for h in range(H):
    for w in range(W):
        if S[h][w] == '#':
            continue
        In = [[False] * W for _ in range(H)]
        In[h][w] = True
        length = 1
        dfs(h, w, h, w)

print(ans if ans >= 4 else -1)