N = int(input())
work = []
for _ in range(N):
    a, b = map(int,input().split())
    work.append((b,a))
    
work.sort()
now = 0
for i in range(N):
    kigen, time = work[i]
    if now + time > kigen:
        print('No')
        exit()
    now += time

print('Yes')