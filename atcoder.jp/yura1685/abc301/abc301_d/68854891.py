S = input()
T = ['0' if S[i] == '?' else S[i] for i in range(len(S))]
N = int(input())

for i in range(len(S)):
    if S[i] != '?':
        continue
    T[i] = '1'
    if int(''.join(T),2) > N:
        T[i] = '0'

X = int(''.join(T),2)
print(X if X <= N else -1)