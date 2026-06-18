N, M = map(int, input().split())
if M < 20 and 2 ** M == N: exit(print('No'))

S_in = [list(input()) for _ in range(N)]
for i in range(N):
    for j in range(M):
        S_in[i][j] = '0' if S_in[i][j] == '1' else '1'
    S_in[i] = int(''.join(S_in[i]), 2)
S = set(S_in)

for i in range(N+2):
    if i not in S:
        print('Yes')
        ans = bin(i)[2:]
        print('0' * (M - len(ans)) + ans)
        break