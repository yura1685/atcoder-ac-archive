S = input()
c = []
if len(S) % 2 == 1:
    print('No')
    exit()
for i in range(len(S)//2):
    if S[2*i] == S[2*i+1]:
        if S[2*i] not in c:
            c.append(S[2*i])
if len(c) == len(S) // 2:
    print('Yes')
else:
    print('No')