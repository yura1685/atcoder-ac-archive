from collections import deque

N = int(input())
if N % 10 == 0: exit(print(-1))
if N < 10: exit(print(N))

pare = [-1] * (N*10)
dq = deque()

for i in range(1,10):
    idx = 11 * i
    if pare[idx] == -1:
        pare[idx]= -2
        dq.append(idx)

ans_idx = -1
while dq:
    new_idx = dq.popleft()
    r, n = divmod(new_idx, 10)
    for k in range(n,10):
        r2 = (10*r+k) % N
        idx2 = r2*10 + k
        if pare[idx2] == -1:
            pare[idx2] = new_idx
            dq.append(idx2)
            if r2 == 0:
                ans_idx = idx2
                break
    if ans_idx != -1:
        break

if ans_idx != -1:
    ans = []
    num = ans_idx
    while num != -2:
        ans.append(str(num % 10))
        num = pare[num]
    ans.reverse()
    print(''.join(ans))

else:
    print(-1)