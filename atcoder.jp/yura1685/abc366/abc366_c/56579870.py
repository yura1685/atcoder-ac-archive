Q = int(input())
M = 10**6 + 1
c = [0]*M
diff = 0
for i in range(Q):
    s = input()
    if s[0] == '1':
        x = int(s[2:])
        if c[x] == 0:
            diff += 1
        c[x] += 1
    elif s[0] == '2':
        x = int(s[2:])
        if c[x] == 1:
            diff -= 1
        c[x] -= 1
    else:
        print(diff)