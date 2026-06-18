N = int(input())

box = [[] for _ in range(N+1)]
num = [[] for _ in range(200001)]

Q = int(input())
for _ in range(Q):
    q = list(map(int,input().split()))
    if q[0] == 1:
        i, j = q[1], q[2]
        box[j].append(i)
        num[i].append(j)
    elif q[0] == 2:
        i = q[1]
        box[i].sort()
        print(*box[i])
    else:
        i = q[1]
        hoge = list(set(num[i]))
        hoge.sort()
        print(*hoge)
        num[i] = hoge