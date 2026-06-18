N = int(input())
a = list(map(int,input().split()))

if sum(a) % N!= 0:
    print(-1)
    exit()

p = sum(a) // N

hasi = 0

now = 0
while now < N:
    count = 0
    hito = 0
    while now + count <= N:
        if now + count == N:
            print(-1)
            exit()
        hito += a[now+count]
        if hito % (count+1) == 0 and hito//(count+1) == p:
            hasi += count
            now += count+1
            break
        count += 1

print(hasi)