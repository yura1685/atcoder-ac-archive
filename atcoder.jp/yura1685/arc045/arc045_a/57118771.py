S = list(map(str,input().split()))
L = []
for i in S:
    if i == 'Left':
        L.append('<')
    elif i == 'Right':
        L.append('>')
    else:
        L.append('A')
print(*L)