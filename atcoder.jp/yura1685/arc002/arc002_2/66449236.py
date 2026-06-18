# 誰だよこのクソ問作ったやつ死ねや

def f(n):
    if n % 400 == 0:
        return 29
    if n % 100 == 0:
        return 28
    if n % 4 == 0:
        return 29
    return 28

Y, M, D = map(int,input().split('/'))

gomi = {1:31,2:f(Y),3:31,4:30,5:31,6:30,7:31,8:31,9:30,10:31,11:30,12:31}

for x in range(D,gomi[M]+1):
    if Y % M == 0 and (Y//M) % x == 0:
        y, m, d = Y, M, x
        m = str(m)
        d = str(x)
        if len(m) == 1:
            m = '0' + m
        if len(d) == 1:
            d = '0' + d
        print(str(y)+'/'+m+'/'+d)
        exit()

M += 1
if M == 13:
    Y +=1
    M = 1

flag = 1
while flag:
    if M == 13:
        Y, M = Y+1, 1
    for x in range(1,gomi[M]+1):
        if Y % M == 0 and (Y//M) % x == 0:
            y, m, d = Y, M, x
            flag = 0
            break
    M += 1

y, m, d = str(y), str(m), str(d)
if len(m) == 1:
    m = '0'+m

if len(d) == 1:
    d = '0' + d

print(y+'/'+m+'/'+d)