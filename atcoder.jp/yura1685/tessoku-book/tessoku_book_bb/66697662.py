Q = int(input())

d = {}

for _ in range(Q):
    q = input().split()
    if q[0] == '1':
        d[q[1]] = int(q[2])
    if q[0] == '2':
        print(d[q[1]])