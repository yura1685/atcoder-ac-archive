S1 = input()
S2 = input()
S3 = input()
T = input()
L = []
for i in range(len(T)):
    if T[i] == '1':
        L.append(S1)
    if T[i] =='2':
        L.append(S2)
    if T[i] == '3':
        L.append(S3)
a = ''.join(L)
print(a)