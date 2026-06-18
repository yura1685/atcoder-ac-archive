X = input()
S = X
while ('oo' in S) or ('ii' in S):
    S = S.replace('ii','ioi')
    S = S.replace('oo','oio')
if S[0] == 'o':
    S = 'i' + S
if S[-1] == 'i':
    S += 'o'    
print(len(S) - len(X))