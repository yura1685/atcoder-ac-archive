a, b, c = map(int,input().split())
if b > c:
    if b < a or a < c:
        print('No');exit()
if c > b:
    if b < a < c:
        print('No');exit()
print('Yes')