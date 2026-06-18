s = input()
x = []
for i in s:
    if i != 'B':
        x.append(i)
    else:
        if x == []:
            pass
        else:
            x.pop()

print(''.join(x))