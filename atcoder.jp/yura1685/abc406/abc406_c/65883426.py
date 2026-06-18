N = int(input())
P = list(map(int,input().split()))

now = 0
up = []
while now < N-1:
    if P[now] < P[now+1]:
        count_up = 0
        while now + count_up < N-1:
            if P[now+count_up] > P[now+count_up+1]:
                break
            count_up += 1
        up.append(count_up)
        now += count_up 
    now += 1

ans = 0
for i in range(len(up)-1):
    ans += up[i]*up[i+1]

print(ans)