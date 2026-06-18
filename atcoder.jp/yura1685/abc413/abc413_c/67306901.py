from collections import deque

A = deque()
Q = int(input()) # (数字，個数)
for _ in range(Q):
    q = list(map(int,input().split()))
    if q[0] == 1:
        if A and A[-1][0] == q[2]:
            num, c = A.pop()
            A.append((num,c+q[1]))
        else:
            A.append((q[2],q[1]))
    else:
        k = q[1]
        S = 0
        cnt = 0
        while cnt < k:
            num, c = A.popleft()
            if cnt + c < k:
                cnt += c
                S += num*c
            else:
                S += num*(k-cnt)
                A.appendleft((num,c-k+cnt))
                break
        print(S)
