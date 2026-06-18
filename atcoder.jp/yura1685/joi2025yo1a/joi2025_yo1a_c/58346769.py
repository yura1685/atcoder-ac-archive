N = int(input())
S = input()
c = ''
for i in S:
    if i == 'J':
        c += 'O'
    elif i == 'O':
        c += 'I'
    else:
        c += 'J'
print(c)