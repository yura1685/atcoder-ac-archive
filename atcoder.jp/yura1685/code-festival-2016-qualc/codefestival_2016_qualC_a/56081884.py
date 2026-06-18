s = input()
if 'C' in s:
    numC = s.index('C')
    if 'F' in s[numC:]:
        print('Yes')
        exit()
print('No')