from collections import deque

N = int(input())
A = list(map(int, input().split()))

ans = 0
dq = deque()
cnt = [0] * 20

for a in A:
    dq.append(a)
    for bit in range(20):
        if a >> bit & 1:
            cnt[bit] += 1
    while dq and max(cnt) > 1:
        a2 = dq.popleft()
        for bit in range(20):
            if a2 >> bit & 1:
                cnt[bit] -= 1
    ans += len(dq)
    
print(ans)