N = int(input())
S = str(input())
T = str(input())
s, t = [], []
for i in range(N):
    s.append(S[i])
    t.append(T[i])
for i in range(N):
    if s[i] == 'l':
        s[i] = '1'
    elif s[i] == 'o':
        s[i] = '0'
    if t[i] == 'l':
        t[i] = '1'
    elif t[i] == 'o':
        t[i] = '0'
for i in range(N):
    if s[i] != t[i]:
        print('No')
        exit()
print('Yes')