H, W = map(int,input().split())
S = ['']*H
for i in range(H):
    S[i] = list(input())

for i in range(H):
    s = S[i]
    for j in range(W-1):
        if s[j] == s[j+1] == 'T':
            s[j], s[j+1] = 'P', 'C'
    print(''.join(s))