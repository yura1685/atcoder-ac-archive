S = input()
if S[0].islower():
    print('No')
else:
    for i in range(1,len(S)):
        if S[i].isupper():
            print('No')
            exit()
    print('Yes')