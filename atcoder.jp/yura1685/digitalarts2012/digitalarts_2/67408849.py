S = list(input())
if S == ['z']*20 or S == ['a']:
    print('NO')
    exit()

T = S.copy()
U = S.copy()
T.sort()
U.reverse()

if S != T:
    print(''.join(T))
elif S != U:
    print(''.join(U))
else:
    a = S[0]
    n = len(S)
    if n == 1:
        S = ['a',chr(ord(a)-1)]
        print(''.join(S))
    elif a == 'a':
        S.pop()
        S[-1] = 'b'
        print(''.join(S))
    elif n == 20:
        S[-1] = chr(ord(a)+1)
        S[-2] = chr(ord(a)-1)
        print(''.join(S))
    else:
        S[-1] = chr(ord(a)-1)
        S.append('a')
        print(''.join(S))