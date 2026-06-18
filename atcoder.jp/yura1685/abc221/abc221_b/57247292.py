S,T = input(),input()
N = len(S)
if S == T:
    print('Yes');exit()
for i in range(N-1):
    if S[i] != T[i]:
        U = S[:i] + S[i+1] + S[i] + S[i+2:]
        break
if U == T:
    print('Yes')
else:
    print('No')