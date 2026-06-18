N, Q = map(int,input().split())
member = [0] * (N+1)
for i in range(Q):
    event = input()
    if event[0] == '1' or event[0] == '2':
        _, x = map(int,event.split())
        member[x] += _
    else:
        _, x = map(int,event.split())
        if member[x] >= 2:
            print('Yes')
        else:
            print('No')