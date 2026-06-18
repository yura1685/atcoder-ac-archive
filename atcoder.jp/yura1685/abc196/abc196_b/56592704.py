x = input()
if '.' in x:
    k = x.index('.')
    print(x[:k])
else:
    print(x)