N, A, B = map(int,input().split())

turn = 1
d = {0:'Bug', 1:'Ant'}
while N > 0:
    if turn:
        N -= A
    else:
        N -= B
    if N <= 0:
        print(d[turn])
    turn = 1-turn