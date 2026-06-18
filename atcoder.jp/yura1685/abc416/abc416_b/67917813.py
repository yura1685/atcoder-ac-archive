S = input()
T = ['.']*len(S)

for i in range(len(S)):
    s = S[i]
    if s == '#':
        T[i] = '#'

n = len(S)
for i in range(n):
    if T[i] == '#':
        if i != 0 and T[i-1] == '.':
            T[i-1] = 'o'
if T[-1] == '.':
    T[-1] = 'o'

print(''.join(T))