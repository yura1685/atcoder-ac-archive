H, W = map(int,input().split())
R = [['.']*W for _ in range(H)]
B = [['.']*W for _ in range(H)]

for h in range(H):
    if h % 2 == 0:
        for w in range(W-1):
            R[h][w] = '#'
        B[h][W-1] = '#'
    else:
        for w in range(1,W):
            B[h][w] = '#'
        R[h][0] = '#'

for h in range(H):
    S = input()
    for w in range(W):
        if S[w] == '#':
            R[h][w] = B[h][w] = '#'

R2 = [''.join(r) for r in R]
B2 = [''.join(b) for b in B]

print(*R2, sep='\n')
print()
print(*B2, sep='\n')