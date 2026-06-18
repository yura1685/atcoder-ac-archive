N = int(input())

le, ri = 1, N
while le <= ri:
    mi = (le+ri)//2
    print('?',mi)
    S = int(input())
    if S == 0:
        le = mi + 1
    else:
        ri = mi - 1
print('!',ri)