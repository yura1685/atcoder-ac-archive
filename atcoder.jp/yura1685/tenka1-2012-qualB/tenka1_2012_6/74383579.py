# ガチのおもんない問題やめてね

S = input()
N = len(S)
alp = set('qwertyuiopasdfghjklzxcvbnm')

if S == '_' * N: exit(print(S))

l, r = 0, 0
while S[l] == '_':
    l += 1
while S[N-r-1] == '_':
    r += 1
S2 = S[l:N-r]

def isCamel(X:str) -> bool:
    if not X or X[0] not in alp: return False
    if '_' in X: return False
    return X.isalnum()

def isUnder(X:str) -> bool:
    if not X: return False
    Ws = X.split('_')
    for W in Ws:
        if not W or W[0] not in alp: return False
        if any(w.isupper() for w in W):
            return False
    return True

isC = isCamel(S2)
isU = isUnder(S2)

if isC == isU:
    exit(print(S))
elif isC:
    ans = []
    for s in S2:
        if s.isupper():
            ans.append('_'+s.lower())
        else:
            ans.append(s)
    print('_' * l + ''.join(ans) + '_' * r)
elif isU:
    ans = []
    i = 0
    L2 = len(S2)
    while i < L2:
        s = S2[i]
        if s != '_':
            ans.append(s)
        else:
            i += 1
            if i < L2:
                ans.append(S2[i].upper())
        i += 1
    print('_' * l + ''.join(ans) + '_' * r)