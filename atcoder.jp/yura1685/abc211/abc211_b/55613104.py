L = []
while True:
    L.append(input())
    if len(L) == 4:
        break
if 'H' in L:
    if '2B' in L:
        if '3B' in L:
            if 'HR' in L:
                print('Yes')
                exit()
print('No')