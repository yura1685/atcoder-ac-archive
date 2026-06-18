N, M = map(int,input().split())

pro = []

for _ in range(N):
    x = list(map(int,input().split()))
    pro.append(x)

for i in range(N-1):
    for j in range(i+1,N):
        A, B = pro[i], pro[j]
        if A[0] > B[0]:
            A, B = B, A
        if A[0] != B[0]:
            Af = A[2:]
            Bf = B[2:]
            fun = [f in Af for f in Bf]
            if all(fun):
                print('Yes')
                exit()
        if A[0] == B[0]:
            Af = A[2:]
            Bf = B[2:]
            fun1 = [f in Af for f in Bf]
            fun2 = [f in Bf for f in Af]
            if (all(fun1) and A[1] > B[1]) or (all(fun2) and A[1] < B[1]):
                print('Yes')
                exit()
print('No')