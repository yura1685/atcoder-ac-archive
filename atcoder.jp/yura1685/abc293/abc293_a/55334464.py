S = input()
L = []
for i in range(len(S)):
    L.append(S[i])
for i in range(len(S)//2):
    L[2*i], L[2*i+1] = L[2*i+1], L[2*i]
a = ''.join(L)
print(a)