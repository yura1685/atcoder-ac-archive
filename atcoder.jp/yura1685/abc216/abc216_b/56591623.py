n = int(input())
S = []
T = []
for i in range(n):
    s, t =map(str,input().split())
    S.append(s)
    T.append(t)

for i in range(n):
    for j in range(i+1,n):
        if S[i] == S[j] and T[i] == T[j]:
            print('Yes')
            exit()
print('No')