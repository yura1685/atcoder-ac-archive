N = int(input())
L = list(map(str, input(). split()))
if 'and' in L:
    print('Yes')
    exit()
if 'not' in L:
    print('Yes')
    exit()
if 'that' in L:
    print('Yes')
    exit()
if 'the' in L:
    print('Yes')
    exit()
if 'you' in L:
    print('Yes')
    exit()
print('No')