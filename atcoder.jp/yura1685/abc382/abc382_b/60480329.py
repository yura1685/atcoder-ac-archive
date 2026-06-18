N, D = map(int,input().split())
S = list(input())
cookie = S.count('@')
cookie_check = 0
for i in range(N):
    if S[i] == '@' and cookie_check >= cookie - D:
        S[i] = '.'
    elif S[i] == '@':
        cookie_check += 1
print(''.join(S))