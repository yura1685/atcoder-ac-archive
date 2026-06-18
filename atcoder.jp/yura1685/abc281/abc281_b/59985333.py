S = input()
alp = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
num = '1234567890'
if S[0] in alp:
    if S[-1] in alp:
        c = S[1:-1]
        if len(c) == 6:
            for i in c:
                if i not in num:
                    print('No')
                    exit()
            if c[0] != '0':
                print('Yes')
                exit()
print('No')