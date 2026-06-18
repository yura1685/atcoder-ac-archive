from collections import defaultdict, deque

H, W, K = map(int, input().split())
P = set()

def f(h, w): return h * W + w

if min(H, W) == 1 and K: exit(print('No'))

dq = deque()
v = defaultdict(bool)

for _ in range(K):
    h, w = map(int, input().split())
    h, w = h-1, w-1
    n = f(h, w)
    P.add(n)
    if w == 0 or h == H-1:
        dq.append((h, w))
        v[n] = True

d = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

while dq:
    h, w = dq.popleft()
    for dh, dw in d:
        nh, nw = h + dh, w + dw
        if not (0 <= nh < H and 0 <= nw < W): continue
        n = f(nh, nw)
        if n not in P: continue
        if not v[n]:
            dq.append((nh, nw))
            v[n] = True
        if nh == 0 or nw == W-1:
            exit(print('No'))

print('Yes')