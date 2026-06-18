N = int(input())
A = list(map(int,input().split()))
Q = int(input())
for i in range(Q):
    query = input()
    if query[0] == '1':
        _, k, x = map(int,query.split())
        A[k-1] = x
    else:
        _, k = map(int,query.split())
        print(A[k-1])