X = input()
while len(X) > 0:
    if X[0] in ['o','k','u']:
        X = X[1:]
    elif len(X) >= 2 and X[:2] == 'ch':
        X = X[2:]
    else:
        print('NO')
        exit()

print('YES')