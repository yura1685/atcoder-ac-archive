N = int(input())
P = list(map(int,input().split()))

oya = {}
for i in range(N-1):
    oya[i+2] = P[i]

sedai = 0
num = N
while num != 1:
    num = oya[num]
    sedai += 1

print(sedai)