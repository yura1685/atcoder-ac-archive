S = input()
for i in range(len(S)):
    if i % 2 == 0:
        if S[i].isupper():
            print('No')
            exit()
    elif i % 2 == 1:
        if S[i].islower():
            print('No')
            exit()
print('Yes')    