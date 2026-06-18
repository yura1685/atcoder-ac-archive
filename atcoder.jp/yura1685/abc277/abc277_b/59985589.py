N = int(input())
mark = 'HDCS'
num  = 'A23456789TJQK'
c = []
for i in range(N):
    S = input()
    if S[0] not in mark:
        print('No')
        exit()
    if S[1] not in num:
        print('No')
        exit()
    c.append(S)

if len(c) == len(set(c)):
    print('Yes')
else:
    print('No')