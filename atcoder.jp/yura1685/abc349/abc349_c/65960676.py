s = input()
T = input()
t = T.lower()

if t[2] == 'x':
    count = 0
    for i in s:
        if i == t[count]:
            count += 1
        if count == 2:
            print('Yes')
            exit()
    print('No')

else:
    count = 0
    for i in s:
        if i == t[count]:
            count += 1
        if count == 3:
            print('Yes')
            exit()
    print('No')