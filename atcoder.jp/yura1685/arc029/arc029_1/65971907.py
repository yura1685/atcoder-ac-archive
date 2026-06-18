from itertools import product
N = int(input())

s = product([0,1], repeat = N)

l = []
for _ in range(N):
    l.append(int(input()))

time = []

for i in s:
    a, b = 0, 0
    for j in range(N):
        if i[j] == 0:
            a += l[j]
        else:
            b += l[j]
    time.append(max(a,b))
print(min(time))