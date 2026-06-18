sa = input()
sb = input()
sc = input()

turn = 'A'
d = {'a':'A','b':'B','c':'C'}

while True:
    if turn == 'A':
        if sa == '':
            print('A')
            exit()
        turn = d[sa[0]]
        sa = sa[1:]
    if turn == 'B':
        if sb == '':
            print('B')
            exit()
        turn = d[sb[0]]
        sb = sb[1:]
    if turn == 'C':
        if sc == '':
            print('C')
            exit()
        turn = d[sc[0]]
        sc = sc[1:]