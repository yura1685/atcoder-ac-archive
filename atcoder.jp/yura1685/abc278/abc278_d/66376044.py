N = int(input())
A = list(map(int,input().split()))

reset = -1
update = [-1]*N
ind = -1

Q = int(input())
for i in range(Q):
    q = list(map(int,input().split()))
    if q[0] == 1:
        reset = q[1]
        ind = i
    elif q[0] == 2:
        if update[q[1]-1] < ind:
            A[q[1]-1] = reset + q[2]
        else:
            A[q[1]-1] += q[2]
        update[q[1]-1] = i
    else:
        if update[q[1]-1] < ind:
            print(reset)
        else:
            print(A[q[1]-1])