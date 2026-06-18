a, b, c, d = map(int,input().split())
turn = 0
while a > 0 and c > 0:
    if turn == 0:
        c -= b
        turn = 1
    elif turn == 1:
        a -= d
        turn = 0
if turn == 1:
    print('Yes')
else:
    print('No')