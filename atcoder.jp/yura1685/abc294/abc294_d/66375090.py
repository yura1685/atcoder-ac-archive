from collections import deque

N, Q = map(int,input().split())
uncall = deque([i for i in range(1,N+1)])
call = deque()
done = [0]*(N+1)

for _ in range(Q):
    q = input()
    if q == '1':
        c = uncall.popleft()
        call.append(c)
    elif q[0] == '2':
        m = int(q[2:])
        done[m] = 1
    else:
        while True:
            c = call.popleft()
            if done[c] == 0:
                call.appendleft(c)
                print(c)
                break
