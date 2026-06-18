N = int(input())
S = input()
cnt = 0
for s in S:
    if s == '(':
        cnt += 1
    else:
        cnt -= 1
    if cnt < 0: exit(print('No'))
print('Yes')