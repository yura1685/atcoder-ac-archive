Q = int(input())

back = [-1]*(Q+1)
front = [-1]*(Q+1)

for i in range(1,Q+1):
    q = list(map(int,input().split()))
    if q[0] == 1:
        x = q[1]
        if back[x] >= 0:
            y = back[x]
            back[i] = y
            front[y] = i
        back[x] = i
        front[i] = x
    else:
        ans = 0
        x, y = q[1:]
        n, m = x, y
        flag = 1
        while True:
            n = back[n]
            m = back[m]
            if n == y:
                flag = 0
                break
            if m == x:
                break
        if flag:
            x, y = y, x
        
        n = back[x]
        while n != y and n >= 0:
            m = back[n]
            back[n] = -1
            front[n] = -1
            ans += n
            n = m
        back[x] = y
        front[y] = x
        print(ans)