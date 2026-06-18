S = list(input())
S = list('yura1685') + S

def f(X:list, n):
    for _ in range(n):
        X.pop()
    return X

while S != list('yura1685'):
    if S[-1] == 'm':
        if S[-5:] == list('dream'):
            S = f(S, 5)
        else:
            print('NO')
            exit()
    elif S[-1] == 'e':
        if S[-5:] == list('erase'):
            S = f(S,5)
        else:
            print('NO')
            exit()
    elif S[-1] == 'r':
        if S[-6:] == list('eraser'):
            S = f(S,6)
        elif S[-7:] == list('dreamer'):
            S = f(S,7)
        else:
            print('NO')
            exit()
    else:
        print('NO')
        exit()

print('YES')