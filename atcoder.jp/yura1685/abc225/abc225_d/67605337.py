from collections import deque

N, Q = map(int,input().split())
trainb = [-1]*(N+1)
trainf = [-1]*(N+1)
for _ in range(Q):
    q = list(map(int,input().split()))
    if q[0] == 1:
        trainb[q[1]] = q[2]
        trainf[q[2]] = q[1]
    if q[0] == 2:
        trainb[q[1]] = -1
        trainf[q[2]] = -1
    if q[0] == 3:
        ans = deque()
        now = q[1]
        while now != -1:
            ans.append(now)
            now = trainb[now]
        now = ans.popleft()
        while now != -1:
            ans.appendleft(now)
            now = trainf[now]
        print(len(ans),*ans)