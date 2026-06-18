N = int(input())
D = 0
while 2 ** D <= N: D += 1

M = 1
turn = 1
while M <= N:
    if turn % 2 == 1:
        M = 2 * M + (D % 2 == 1)
    else:
        M = 2 * M + (D % 2 == 0)
    turn += 1

print('Takahashi' if turn % 2 == 1 else 'Aoki')