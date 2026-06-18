N = int(input())
S = list(input())
a = 0
for i in range(N):
    if S[i] == ',' and a == 0:
        S[i] = '.'
    if S[i] == '"':
        a = (a+1)%2
print(''.join(S))