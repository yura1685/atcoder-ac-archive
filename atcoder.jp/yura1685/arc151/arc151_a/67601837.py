N = int(input())
S = input()
T = input()
U = []
q = 0

for i in range(N):
    if S[i] == T[i]:
        U += ['0']
    else:
        q += 1
        U += ['?']

if q % 2 == 1:
    print(-1)
    exit()

s, t = q//2, q//2

for i in range(N):
    if U[i] == '0':
        continue
    if S[i] == '1' and s:
        U[i] = '0'
        s -= 1
    elif T[i] == '1' and t:
        U[i] = '0'
        t -= 1
    else:
        U[i] = '1'
        if S[i] == '0':
            s -= 1
        else:
            t -= 1

print(''.join(U))