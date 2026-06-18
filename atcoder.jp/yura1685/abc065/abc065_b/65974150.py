N = int(input())
d = {}
for i in range(1,N+1):
    a = int(input())
    d[i] = a

now = 1
push = 0
pushed = [0]*(N+1)
while now != 2:
    if pushed[now] == 1:
        print(-1)
        exit()
    pushed[now] += 1
    now = d[now]
    push += 1
print(push)