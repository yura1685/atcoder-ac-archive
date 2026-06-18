S = input()
T = input()

n = len(S)
for i in range(1,n):
    if S[i].isupper():
        if S[i-1] not in T:
            print('No')
            exit()
print('Yes')