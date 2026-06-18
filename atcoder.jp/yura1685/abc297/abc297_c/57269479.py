H, W = map(int,input().split())
for i in range(H):
    s = list(input())
    for j in range(W-1):
        if s[j] == s[j+1] == 'T':
            s[j], s[j+1] = 'P', 'C'
    print(''.join(s))