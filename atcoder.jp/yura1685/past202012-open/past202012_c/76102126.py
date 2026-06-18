N = int(input())
if N == 0: exit(print(0))
ans = []
tr = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
while N:
    x = N % 36
    ans.append(tr[x])
    N //= 36

ans.reverse()
print(''.join(ans))