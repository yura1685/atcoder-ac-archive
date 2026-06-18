S = input()
L = []
for i in range(1,len(S)+1):
    for j in range(len(S)+1-i):
        L.append(S[j:j+i])
print(len(set(L)))