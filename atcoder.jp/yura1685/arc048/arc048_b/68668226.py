from itertools import accumulate

hand = [[0]*(100001) for _ in range(3)]
# hand[i][j]: 手iであってRatingがj以下の総数

N = int(input())
P = []
for _ in range(N):
    R, H = map(int,input().split())
    hand[H-1][R] += 1
    P.append((R,H-1))

hand2 = [list(accumulate(X)) for X in hand]

for r, h in P:
    win = sum(hand2[i][r-1] for i in range(3)) + hand[(h+1)%3][r]
    draw = hand[h][r]-1
    lose = N - win - draw - 1
    print(win, lose, draw)