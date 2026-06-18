X = list(input())
S = X
T = list(reversed(X))

anss = 0
anst = 0

for i in range(1,len(S)):
    if S[i-1] == S[i] == '1':
        S[i] = '0'
        anss += 1
    elif S[i-1] == S[i] == '0':
        S[i] = '1'
        anss += 1

for i in range(1,len(T)):
    if T[i-1] == T[i] == '1':
        T[i] = '0'
        anst += 1
    elif T[i-1] == T[i] == '0':
        T[i] = '1'
        anst += 1 

print(min(anss,anst))