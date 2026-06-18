S = input()
S = S.upper()
if 'I' in S:
    S = S[S.index('I')+1:]
    if 'C' in S:
        S = S[S.index('C')+1:]
        if 'T' in S:
            print('YES')
            exit()
print('NO')