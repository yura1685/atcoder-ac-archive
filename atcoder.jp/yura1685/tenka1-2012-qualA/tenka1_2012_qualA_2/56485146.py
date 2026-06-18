L = list(input())
W = []
a = 0
for i in range(len(L)):
    if L[i] == ' ' and a == 0:
        a = 1
    elif L[i] != ' ' and a == 1:
        W.append(',')
        a = 0
    if L[i] != ' ':
        W.append(L[i])
print(''.join(W))