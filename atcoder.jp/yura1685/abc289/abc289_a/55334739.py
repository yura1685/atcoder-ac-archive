S = input()
L = []
for i in range(len(S)):
    L.append(S[i])
for i in range(len(L)):
    if L[i] == '1':
        L[i] = '0'
    elif L[i] == '0':
        L[i] = '1'
a = ''.join(L)
print(a)