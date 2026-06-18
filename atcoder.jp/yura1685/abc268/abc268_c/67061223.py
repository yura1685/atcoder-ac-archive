N = int(input())
P = list(map(int,input().split()))
d = [0]*N

for i in range(N):
    p = P[i]
    dis = [(i-p+x-1)%N for x in range(3)]
    for j in dis:
        d[j] += 1

print(max(d))