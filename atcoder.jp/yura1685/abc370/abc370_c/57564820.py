S = input()
T = input()
n = len(S)
L = []

while S != T:
    zzz = 'z'*n
    for i in range(n):
        if S[i] != T[i]:
            zzz = min(zzz,S[:i] + T[i] + S[i+1:])
    L.append(zzz)
    S = zzz

print(len(L))
print('\n'.join(L))