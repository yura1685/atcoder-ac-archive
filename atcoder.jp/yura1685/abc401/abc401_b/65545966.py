N = int(input())
now = 'logout'
error = 0
for i in range(N):
    S = input()
    if S[0] == 'l':
        now = S
    if S == 'private' and now == 'logout':
        error += 1
print(error)