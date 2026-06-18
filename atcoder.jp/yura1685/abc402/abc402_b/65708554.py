Q = int(input())
line = []

for i in range(Q):
    q = input()
    if q == '2':
        print(line[0])
        line = line[1:]
    else:
        line.append(q[2:])