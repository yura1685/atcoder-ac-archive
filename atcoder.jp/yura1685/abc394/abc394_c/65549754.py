S = list(input())
n = len(S)
i = 0
while i != n-1:
    if S[i] == 'W' and S[i+1] == 'A':
        S[i], S[i+1] = 'A', 'C'
        i -= 1
    else:
        i += 1
    if i == -1:
        i = 0
print(''.join(S))