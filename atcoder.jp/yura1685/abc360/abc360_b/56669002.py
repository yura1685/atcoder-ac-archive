s, t = map(str,input().split())
L = len(s)
for w in range(1,L):
    for c in range(w):
        u = ''
        k = 0
        while c+k<L:
            u += s[c+k]
            k += w
        if u == t:
            print('Yes');exit()
print('No')