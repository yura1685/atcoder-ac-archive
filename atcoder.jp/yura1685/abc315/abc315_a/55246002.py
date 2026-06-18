S = input()
L = []
for i in range(len(S)):
    if S[i] != 'a' and S[i] != 'i' and S[i] != 'u' and S[i] != 'e' and S[i] != 'o':
        L.append(S[i])
a = ''.join(L)
print(a)