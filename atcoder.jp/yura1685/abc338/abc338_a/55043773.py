S = input()
a = 0
if S[0].islower():
    print('No')
else:
    for i in range(1,len(S)):
        if S[i].isupper():
            print('No')
            a = 1
            break
    if a == 0:
        print('Yes')