N, M = map(int,input().split())
split = []
A = list(map(int,input().split()))
i = 1
while i <= N:
    c = []
    j = 0
    flag = 0
    while i+j in A:
        c.append(i+j)
        j += 1
        flag = 1
    if flag == 1:
        split += reversed(c+[c[-1]+1])
    else:
        split += [i]
    i += j+1
print(*split)