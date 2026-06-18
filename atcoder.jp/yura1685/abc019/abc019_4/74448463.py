N = int(input())

M, u = 0, 0
for i in range(2, N+1):
    print('?', 1, i)
    d = int(input())
    if M < d:
        M = d
        u = i

ans = 0
for i in range(1, N+1):
    if i == u:
        continue
    print('?', i, u)
    d = int(input())
    ans = max(ans, d)

print('!', ans)