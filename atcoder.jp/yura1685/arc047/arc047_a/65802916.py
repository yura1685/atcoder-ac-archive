N, L = map(int,input().split())
S = input()
tab = 1
clash = 0
for i in S:
    if i == '+':
        tab += 1
        if tab > L:
            tab = 1
            clash += 1
    elif i == '-':
        tab = max(1,tab-1)
print(clash)