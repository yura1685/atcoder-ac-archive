N = int(input())
S = list(input().split())
ans = []
for ss in S:
    s = ss[0]
    if s <= 'c':
        C = 2
    elif s <= 'f':
        C = 3
    elif s <= 'i':
        C = 4
    elif s <= 'l':
        C = 5
    elif s <= 'o':
        C = 6
    elif s <= 's':
        C = 7
    elif s <= 'v':
        C = 8
    else:
        C = 9
    ans.append(str(C))

print(''.join(ans))