#ABC337C - Lining Up 2

N = int(input())
A = list(map(int,input().split()))
d = {}

for i in range(N):
    a = A[i]
    if a == -1:
        sentou = i+1
    else:
        d[a] = i+1

retu = [sentou]
hum = sentou

for _ in range(N-1):
    hum = d[hum]
    retu.append(hum)

print(*retu)