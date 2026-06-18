N, Q = map(int,input().split())

A = [i for i in range(1,N+1)]
rot = 0

for _ in range(Q):
    q = input().split()
    if q[0] == '1':
        A[(int(q[1]) + rot) % N -1] = int(q[2])
    elif q[0] == '2':
        print(A[(int(q[1]) + rot) % N -1])
    else:
        rot = (rot+int(q[1])) % N

