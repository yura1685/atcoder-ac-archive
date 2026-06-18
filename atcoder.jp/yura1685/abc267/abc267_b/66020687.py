S = input()
if S[0] == '1':
    print('No')
    exit()

L1 = [int(S[6])]
L2 = [int(S[3])]
L3 = [int(S[1]), int(S[7])]
L4 = [int(S[0]), int(S[4])]
L5 = [int(S[2]), int(S[8])]
L6 = [int(S[5])]
L7 = [int(S[9])]

L = [L1,L2,L3,L4,L5,L6,L7]
for i in range(5):
    for j in range(7):
        for p in range(i+1,j):
            if sum(L[i]) != 0 and sum(L[j]) != 0 and sum(L[p]) == 0:
                print('Yes')
                exit()
print('No')