N = int(input())
S = input()
L = []
a = 0
while a <= N - 1:
    if a == N - 1:
        L.append(S[a])
        break
    elif S[a] == 'n' and S[a+1] == 'a':
        L.append(S[a])
        L.append('y')
        L.append(S[a+1])
        a += 2
    else:
        L.append(S[a])
        a += 1
b = ''.join(L)
print(b)