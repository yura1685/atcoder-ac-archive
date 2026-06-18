from collections import deque

N = int(input())
dq = deque(map(int,input().split()))
ans = 0

while len(dq) > 1:
    a, b = dq.popleft(), dq.popleft()
    dq.appendleft(b); dq.appendleft(a)
    d, c = dq.pop(), dq.pop()
    dq.append(c); dq.append(d)
    if 2*a + b <= c + 2*d:
        ans += 2*a + b + 1
        dq.popleft(); dq.popleft()
        n = dq.popleft()
        dq.appendleft(a+b+2+n)
    else:
        ans += 2*d + c + 1
        dq.pop(); dq.pop()
        n = dq.pop()
        dq.append(d+c+2+n)

print(ans)