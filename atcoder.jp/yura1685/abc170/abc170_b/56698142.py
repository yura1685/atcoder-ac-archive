X, Y = map(int,input().split())
for kame in range(X+1):
    turu = X - kame
    if 4*kame + 2*turu == Y:
        print('Yes');exit()
print('No')