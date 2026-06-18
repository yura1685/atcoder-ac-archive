from collections import deque

tutu = deque()
Q = int(input())
for _ in range(Q):
    q = list(map(int,input().split()))
    if q[0] == 1:
        tutu.append((q[1], q[2]))
    else:
        c = q[1]
        ans = 0
        ballc = 0
        while True:
            num, cou = tutu.popleft()
            if ballc + cou > c:
                ans += num*(c-ballc)
                tutu.appendleft((num,cou-c+ballc))
                break
            if ballc + cou == c:
                ans += num*cou
                break
            ans += num*cou
            ballc += cou
        print(ans)