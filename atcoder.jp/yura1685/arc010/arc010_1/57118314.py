N, M, A, B = map(int,input().split())
meisi = N
day = 1
for _ in range(M):
    c = int(input())
    if meisi <= A:
        meisi += B
    meisi -= c
    if meisi < 0:
        print(day);exit()
    day += 1
print('complete')