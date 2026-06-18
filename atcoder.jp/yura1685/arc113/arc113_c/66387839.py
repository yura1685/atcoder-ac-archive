S = input()
N = len(S)

alp = ''

L = [] 
start = -1
delete = 0

for i in range(N-1):
    if S[i] == S[i+1]:
        if S[i] != alp:
            if alp:
                L.append((start, delete-2))
            start = i
            alp = S[i]
            delete = 0
                
        else:
            pass
    if S[i] == alp:
        delete += 1

if S[N-1] == alp:
    delete += 1
if start != -1:
    L.append((start, delete-2))

ans = 0
if L:
    for s, d in L:
        ans += N - s - d - 2

print(ans)