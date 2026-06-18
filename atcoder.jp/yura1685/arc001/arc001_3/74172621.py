c = [input() for _ in range(8)]

def f(h, w): return 8 * h + w
Q = set()
for h in range(8):
    for w in range(8):
        if c[h][w] == 'Q':
            Q.add(f(h, w))

for hw in Q:
    for hw2 in Q:
        h, w = divmod(hw, 8)
        h2, w2 = divmod(hw2, 8)
        if h == h2 and w == w2:
            continue
        dh, dw = abs(h-h2), abs(w-w2)
        if dh == 0 or dw == 0 or dh == dw:
            exit(print('No Answer'))

def dfs(S:set):
    if len(S) == 8:
        ans = [['.'] * 8 for _ in range(8)]
        for hw in S:
            h, w = divmod(hw, 8)
            ans[h][w] = 'Q'
        for a in ans: print(''.join(a))
        exit()
    h = 0
    H = {divmod(hw, 8)[0] for hw in S}
    while h in H: h += 1
    for w in range(8):
        flag = True
        for i in range(1,8):
            hmi, hpi = 0 <= h-i < 8, 0 <= h+i < 8
            wmi, wpi = 0 <= w-i < 8, 0 <= w+i < 8
            if hmi and f(h-i, w) in S: flag = False
            if hpi and f(h+i, w) in S: flag = False
            if wmi and f(h, w-i) in S: flag = False
            if wpi and f(h, w+i) in S: flag = False
            if hmi and wmi and f(h-i, w-i) in S: flag = False
            if hmi and wpi and f(h-i, w+i) in S: flag = False
            if hpi and wmi and f(h+i, w-i) in S: flag = False
            if hpi and wpi and f(h+i, w+i) in S: flag = False
            if not flag: break
        else: n = f(h, w); S.add(n); dfs(S); S.discard(n)

dfs(Q)
print('No Answer')