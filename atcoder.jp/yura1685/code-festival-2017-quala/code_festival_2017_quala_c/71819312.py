from collections import defaultdict

H, W = map(int,input().split())
S = [input() for _ in range(H)]

alp = [0] * 26
for h in range(H):
    for w in range(W):
        alp[ord(S[h][w])-97] += 1

X = [n for n in alp if n]
d = defaultdict(int)
d[4] = H*W//4
if H % 2 == 1: d[2] += W//2
if W % 2 == 1: d[2] += H//2
if H*W%2 == 1: d[1] = 1

while X:
    u = X.pop()
    while u:
        if u >= 4 and d[4] > 0:
            u -= 4
            d[4] -= 1
        elif u >= 4 and d[4] == 0 and d[2] > 0:
            u -= 2
            d[2] -= 1
        elif 2 <= u < 4 and d[2] > 0:
            u -= 2
            d[2] -= 1
        elif u == 1 and d[1] > 0:
            u -= 1
            d[1] -= 1
        else:
            exit(print('No'))

print('Yes')