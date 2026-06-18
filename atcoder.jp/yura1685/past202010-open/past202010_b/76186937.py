X, Y = map(int, input().split())
if Y == 0: exit(print('ERROR'))
Z = str(X/Y) + '00'
i = Z.index('.')
print(Z[:i+3])