K = int(input())
S = input(); n = len(S)
T = input(); m = len(T)

if abs(n-m) > 1:
    print('No')
    exit()

if n == m:
    dif = 0
    for i in range(n):
        if S[i] != T[i]:
            dif += 1
    print('Yes' if dif < 2 else 'No')
    exit()

if m < n:
    S, T = T, S #Sを短い方とする

ans = []
for i in range(min(m,n)):
    if S[i] == T[i]:
        ans.append(S[i])
    else:
        ans += T[i+1:]
        break

if not ans or S == ''.join(ans):
    print('Yes')
else:
    print('No')